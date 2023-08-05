import brkt_cli
import logging

from brkt_cli.subcommand import Subcommand

from brkt_cli import encryptor_service, util
from brkt_cli.instance_config import INSTANCE_METAVISOR_MODE
from brkt_cli.instance_config_args import (
    instance_config_from_values,
    setup_instance_config_args
)
from brkt_cli.gce import (
    encrypt_gce_image,
    encrypt_gce_image_args,
    gce_service,
    launch_gce_image,
    launch_gce_image_args,
    update_gce_image,
    update_encrypted_gce_image_args,
)
from brkt_cli.validation import ValidationError

log = logging.getLogger(__name__)


class EncryptGCEImageSubcommand(Subcommand):

    def name(self):
        return 'encrypt-gce-image'

    def register(self, subparsers):
        encrypt_gce_image_parser = subparsers.add_parser(
            'encrypt-gce-image',
            formatter_class=brkt_cli.SortingHelpFormatter
        )
        encrypt_gce_image_args.setup_encrypt_gce_image_args(encrypt_gce_image_parser)
        setup_instance_config_args(encrypt_gce_image_parser,
                                   brkt_env_default=brkt_cli.BRKT_ENV_PROD)

    def run(self, values):
        return _run_subcommand(self.name(), values)


class UpdateGCEImageSubcommand(Subcommand):

    def name(self):
        return 'update-gce-image'

    def register(self, subparsers):
        update_gce_image_parser = subparsers.add_parser(
            'update-gce-image',
            formatter_class=brkt_cli.SortingHelpFormatter
        )
        update_encrypted_gce_image_args.setup_update_gce_image_args(update_gce_image_parser)
        setup_instance_config_args(update_gce_image_parser,
                                   brkt_env_default=brkt_cli.BRKT_ENV_PROD)

    def run(self, values):
        return _run_subcommand(self.name(), values)


class LaunchGCEImageSubcommand(Subcommand):

    def name(self):
        return 'launch-gce-image'

    def register(self, subparsers):
        launch_gce_image_parser = subparsers.add_parser(
            'launch-gce-image',
            formatter_class=brkt_cli.SortingHelpFormatter
        )
        launch_gce_image_args.setup_launch_gce_image_args(launch_gce_image_parser)
        setup_instance_config_args(launch_gce_image_parser,
                                   mode=INSTANCE_METAVISOR_MODE)

    def run(self, values):
        return _run_subcommand(self.name(), values)


def get_subcommands():
    return [EncryptGCEImageSubcommand(),
            UpdateGCEImageSubcommand(),
            LaunchGCEImageSubcommand()]


def _run_subcommand(subcommand, values):
    if subcommand == 'encrypt-gce-image':
        return command_encrypt_gce_image(values, log)
    if subcommand == 'update-gce-image':
        return command_update_encrypted_gce_image(values, log)
    if subcommand == 'launch-gce-image':
        return command_launch_gce_image(values, log)


def command_launch_gce_image(values, log):
    gce_svc = gce_service.GCEService(values.project, None, log)
    instance_config = instance_config_from_values(values)
    if values.startup_script:
        extra_items = [{'key': 'startup-script', 'value': values.startup_script}]
    else:
        extra_items = None
    brkt_userdata = instance_config.make_userdata()
    metadata = gce_service.gce_metadata_from_userdata(brkt_userdata,
                                                      extra_items=extra_items)
    launch_gce_image.launch(log,
                            gce_svc,
                            values.image,
                            values.instance_name,
                            values.zone,
                            values.delete_boot,
                            values.instance_type,
                            metadata)
    return 0


def command_update_encrypted_gce_image(values, log):
    session_id = util.make_nonce()
    gce_svc = gce_service.GCEService(values.project, session_id, log)
    check_args(values, gce_svc)

    encrypted_image_name = gce_service.get_image_name(values.encrypted_image_name, values.image)

    gce_service.validate_image_name(encrypted_image_name)

    log.info('Starting updater session %s', gce_svc.get_session_id())
    updated_image_id = update_gce_image.update_gce_image(
        gce_svc=gce_svc,
        enc_svc_cls=encryptor_service.EncryptorService,
        image_id=values.image,
        encryptor_image=values.encryptor_image,
        encrypted_image_name=encrypted_image_name,
        zone=values.zone,
        instance_config=instance_config_from_values(values),
        keep_encryptor=values.keep_encryptor,
        image_file=values.image_file,
        image_bucket=values.bucket,
        network=values.network
    )

    print(updated_image_id)
    return 0


def command_encrypt_gce_image(values, log):
    session_id = util.make_nonce()
    gce_svc = gce_service.GCEService(values.project, session_id, log)
    check_args(values, gce_svc)

    encrypted_image_name = gce_service.get_image_name(values.encrypted_image_name, values.image)
    gce_service.validate_image_name(encrypted_image_name)

    log.info('Starting encryptor session %s', gce_svc.get_session_id())
    encrypted_image_id = encrypt_gce_image.encrypt(
        gce_svc=gce_svc,
        enc_svc_cls=encryptor_service.EncryptorService,
        image_id=values.image,
        encryptor_image=values.encryptor_image,
        encrypted_image_name=encrypted_image_name,
        zone=values.zone,
        instance_config=instance_config_from_values(values),
        image_project=values.image_project,
        keep_encryptor=values.keep_encryptor,
        image_file=values.image_file,
        image_bucket=values.bucket,
        network=values.network
    )
    # Print the image name to stdout, in case the caller wants to process
    # the output.  Log messages go to stderr.
    print(encrypted_image_id)
    return 0


def check_args(values, gce_svc):
    if not gce_svc.network_exists(values.network):
        raise ValidationError("Network provided does not exist")
    if values.encryptor_image:
        if values.bucket != 'prod':
            raise ValidationError("Please provided either an encryptor image or an image bucket")
    if not values.token:
        raise ValidationError('Must provide a token')

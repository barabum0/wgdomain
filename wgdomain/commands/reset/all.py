import click

from wgdomain.tools.config import parse_config_file
from wgdomain.tools.qr import print_qr


@click.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.option('--qr', is_flag=True, default=False, help="Generate a QR code of a config file")
@click.option('--no-save', is_flag=True, default=False, help="Don't save the config to file")
def reset_all(config_file: str, qr: bool, no_save: bool):
    """Resets configuration to accept all domains."""

    config = parse_config_file(config_file)
    config.set("Peer", "AllowedIPs", "0.0.0.0/0, ::/0")

    if not no_save:
        with open(config_file, "w") as cfg_file:
            config.write(cfg_file)

    click.echo(f"Resetting {config_file} to accept all domains.")

    if qr:
        print_qr(config)

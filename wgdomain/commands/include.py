import click

from wgdomain.tools.config import parse_config_file
from wgdomain.tools.domain import get_A_records
from wgdomain.tools.qr import print_qr


@click.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
@click.option('--qr', is_flag=True, default=False, help="Generate a QR code of a config file")
@click.option('--no-save', is_flag=True, default=False, help="Don't save the config to file")
def include(config_file: str, domain: str, qr: bool, no_save: bool):
    """Includes a domain or IP for routing through Wireguard."""

    config = parse_config_file(config_file)

    ips = get_A_records(domain)
    ips = [f"{ip}/32" for ip in ips]

    allowed_ips = config.get("Peer", "AllowedIPs").split(",")
    allowed_ips = [ip.strip() for ip in allowed_ips]
    allowed_ips += ips
    allowed_ips = list(set(allowed_ips))

    config.set("Peer", "AllowedIPs", ", ".join(allowed_ips))

    if not no_save:
        with open(config_file, "w") as cfg_file:
            config.write(cfg_file)

    click.echo(f"Domain {domain} was included.")

    if qr:
        print_qr(config)

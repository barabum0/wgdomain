import click

from wgdomain.tools.config import parse_config_file
from wgdomain.tools.domain import get_A_records
from wgdomain.tools.ip_excluder import exclude_ip_networks
from wgdomain.tools.qr import print_qr


@click.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
@click.option('--qr', is_flag=True, default=False, help="Generate a QR code of a config file")
@click.option('--no-save', is_flag=True, default=False, help="Don't save the config to file")
def exclude(config_file: str, domain: str, qr: bool, no_save: bool):
    """Excludes a domain or IP from routing through Wireguard."""

    config = parse_config_file(config_file)

    ips = get_A_records(domain)
    ips = [f"{ip}/32" for ip in ips]
    excluded_ips = ", ".join(ips)

    allowed_ips = config.get("Peer", "AllowedIPs")

    allowed_ips = exclude_ip_networks(allowed_ips, excluded_ips)

    config.set("Peer", "AllowedIPs", allowed_ips)

    if not no_save:
        with open(config_file, "w") as cfg_file:
            config.write(cfg_file)

    click.echo(f"Domain {domain} was excluded.")

    if qr:
        print_qr(config)

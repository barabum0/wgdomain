import click

from wgdomain.commands import cli


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
def exclude(config_file: str, domain: str):
    """Excludes a domain or IP from routing through Wireguard."""
    # Code to exclude domain/IP
    click.echo(f"Excluding {domain} from {config_file}.")

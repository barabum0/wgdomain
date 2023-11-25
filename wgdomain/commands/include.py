import click

from wgdomain.commands import cli


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
def include(config_file: str, domain: str):
    """Includes a domain or IP for routing through Wireguard."""
    # Code to include domain/IP
    click.echo(f"Including {domain} in {config_file}.")

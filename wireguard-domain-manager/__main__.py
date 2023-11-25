import click
import click_completion

from __init__ import cli, reset

click_completion.init()


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
def include(config_file: str, domain: str):
    """Includes a domain or IP for routing through Wireguard."""
    # Code to include domain/IP
    click.echo(f"Including {domain} in {config_file}.")


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
def exclude(config_file: str, domain: str):
    """Excludes a domain or IP from routing through Wireguard."""
    # Code to exclude domain/IP
    click.echo(f"Excluding {domain} from {config_file}.")


@reset.command(name='all')
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
def reset_all(config_file: str):
    """Resets configuration to accept all domains."""
    # Code to reset configuration to accept all domains
    click.echo(f"Resetting {config_file} to accept all domains.")


@reset.command(name='none')
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
def reset_none(config_file: str):
    """Resets configuration to exclude all domains."""
    # Code to reset configuration to exclude all domains
    click.echo(f"Resetting {config_file} to exclude all domains.")


if __name__ == '__main__':
    cli()

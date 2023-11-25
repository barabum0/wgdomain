import click

from wgdomain.commands.reset import reset


@reset.command(name='none')
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
def reset_none(config_file: str):
    """Resets configuration to exclude all domains."""
    # Code to reset configuration to exclude all domains
    click.echo(f"Resetting {config_file} to exclude all domains.")

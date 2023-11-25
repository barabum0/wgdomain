import click

from wgdomain.commands.reset import reset


@reset.command(name='all')
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
def reset_all(config_file: str):
    """Resets configuration to accept all domains."""
    # Code to reset configuration to accept all domains
    click.echo(f"Resetting {config_file} to accept all domains.")

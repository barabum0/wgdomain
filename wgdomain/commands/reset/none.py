import click

from wgdomain.tools.config import parse_config_file


@click.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
def reset_none(config_file: str):
    """Resets configuration to exclude all domains."""

    config = parse_config_file(config_file)
    config.remove_option("Peer", "AllowedIPs")

    with open(config_file, "w") as cfg_file:
        config.write(cfg_file)

    click.echo(f"Resetting {config_file} to exclude all domains.")

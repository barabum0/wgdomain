import click

from wgdomain.tools.config import parse_config_file


@click.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
def reset_all(config_file: str):
    """Resets configuration to accept all domains."""

    config = parse_config_file(config_file)
    config.set("Peer", "AllowedIPs", "0.0.0.0/0, ::/0")

    with open(config_file, "w") as cfg_file:
        config.write(cfg_file)

    click.echo(f"Resetting {config_file} to accept all domains.")

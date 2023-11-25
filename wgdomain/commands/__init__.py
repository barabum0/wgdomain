import click


@click.group()
def cli():
    """Manages domains and IPs in Wireguard configurations."""
    pass


@cli.group()
def reset():
    """Resets configuration settings."""
    pass

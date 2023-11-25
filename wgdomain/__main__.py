import click_completion

from wgdomain.commands import cli

click_completion.init()


if __name__ == '__main__':
    cli()

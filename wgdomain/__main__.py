import click_completion

from commands import cli, reset
from commands.exclude import exclude
from commands.include import include
from commands.reset.all import reset_all
from commands.reset.none import reset_none

click_completion.init()

cli.add_command(include, name="include")
cli.add_command(exclude, name="exclude")
reset.add_command(reset_all, name="all")
reset.add_command(reset_none, name="none")


if __name__ == '__main__':
    cli()

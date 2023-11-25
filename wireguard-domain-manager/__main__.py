import click
import click_completion

click_completion.init()


@click.group()
def cli():
    """Управляет доменами и IP-адресами в конфигурации Wireguard."""
    pass


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
def include(config_file, domain):
    """Добавляет домен или IP-адрес для маршрутизации через Wireguard."""
    # Код для добавления домена/IP
    click.echo(f"Добавление {domain} в {config_file}.")


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('domain')
def exclude(config_file, domain):
    """Исключает домен или IP-адрес из маршрутизации через Wireguard."""
    # Код для исключения домена/IP
    click.echo(f"Исключение {domain} из {config_file}.")


@cli.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('setting', type=click.Choice(['all', 'none'], case_sensitive=False))
def reset(config_file, setting):
    """Сбрасывает настройки конфигурации для принятия всех или никаких доменов."""
    if setting == 'all':
        # Код для сброса конфигурации, чтобы принимать все домены
        click.echo(f"Сброс {config_file} для принятия всех доменов.")
    elif setting == 'none':
        # Код для сброса конфигурации, чтобы не принимать ни одного домена
        click.echo(f"Сброс {config_file} для исключения всех доменов.")


if __name__ == '__main__':
    cli()

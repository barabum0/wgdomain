import click
import click_completion

click_completion.init()


@click.command()
@click.argument('config_file', type=click.Path())
@click.argument('action', type=click.Choice(['include', 'exclude'], case_sensitive=False))
@click.argument('domain')
def wgdomain(config_file, action, domain):
    """
    Управляет доменами и IP-адресами в конфигурации Wireguard.

    CONFIG_FILE: Путь к файлу конфигурации Wireguard.
    ACTION: 'include' для добавления, 'exclude' для исключения домена/IP.
    DOMAIN: Домен или IP-адрес для обработки.
    """
    # Логика обработки команды
    if action == 'include':
        # Код для добавления домена/IP
        click.echo(f"Добавление {domain} в {config_file}.")
    elif action == 'exclude':
        # Код для исключения домена/IP
        click.echo(f"Исключение {domain} из {config_file}.")


if __name__ == '__main__':
    wgdomain()

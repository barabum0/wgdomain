import click
import click_completion

click_completion.init()


@click.command()
@click.argument('config_file', type=click.Path(exists=True, dir_okay=False))
@click.argument('action', type=click.Choice(['include', 'exclude'], case_sensitive=False))
@click.argument('domain')
def app(config_file, action, domain):
    """
    Управляет доменами и IP-адресами в конфигурации Wireguard.

    CONFIG_FILE: Путь к файлу конфигурации Wireguard.
    ACTION: 'include' для добавления, 'exclude' для исключения домена/IP.
    DOMAIN: Домен или IP-адрес для обработки.
    """

    match action:
        case "include":
            # Код для добавления домена/IP
            click.echo(f"Добавление {domain} в {config_file}.")
        case "exclude":
            # Код для исключения домена/IP
            click.echo(f"Исключение {domain} из {config_file}.")


if __name__ == '__main__':
    app()

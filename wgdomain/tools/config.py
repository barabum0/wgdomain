import configparser


def parse_config_file(config_file_path: str) -> configparser.ConfigParser:
    """Открывает и парсит файл конфигурации Wireguard."""
    config = configparser.ConfigParser()
    config.optionxform = str
    config.read(config_file_path)
    return config

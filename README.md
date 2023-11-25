# Wireguard Domain Manager

## Описание
Wireguard Domain Manager - это инструмент командной строки для управления доменами и IP-адресами в конфигурации VPN Wireguard. Он позволяет легко включать, исключать домены, а также сбрасывать настройки для определенного поведения маршрутизации.

## Установка
Опишите здесь, как установить ваш инструмент. Например, если вы используете `poetry`, то:
```bash
pipx install git+https://github.com/barabum0/wgdomain
wgdomain --help
```

## Использование
Примеры использования команд:

### Добавление домена
Чтобы добавить домен или IP-адрес для маршрутизации через Wireguard:
```bash
wgdomain include /path/to/wireguard.conf example.com
```

### Исключение домена
#### Данная функция основана на [ZerGo0/WireGuard-Allowed-IPs-Excluder](https://github.com/ZerGo0/WireGuard-Allowed-IPs-Excluder) _(упрощено ChatGPT)_
Чтобы исключить домен или IP-адрес из маршрутизации через Wireguard:
```bash
wgdomain exclude /path/to/wireguard.conf example.com
```

### Сброс настроек
#### Принять все домены
Чтобы сбросить конфигурацию так, чтобы принимались все домены:
```bash
wgdomain reset all /path/to/wireguard.conf
```

#### Не принимать ни одного домена
Чтобы сбросить конфигурацию так, чтобы исключались все домены:
```bash
wgdomain reset none /path/to/wireguard.conf
```
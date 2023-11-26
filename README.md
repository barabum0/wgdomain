# Wireguard Domain Manager

## Description
Wireguard Domain Manager is a command-line tool for managing domains and IP addresses in Wireguard VPN configuration. It enables easy inclusion and exclusion of domains, as well as resetting settings for specific routing behaviors.

## Installation
```bash
pipx install git+https://github.com/barabum0/wgdomain
wgdomain --help
```

## Usage
Examples of using commands:

### Adding a Domain
To add a domain or IP address for routing through Wireguard:
```bash
wgdomain include /path/to/wireguard.conf example.com
```

### Excluding a Domain
#### This feature is based on [ZerGo0/WireGuard-Allowed-IPs-Excluder](https://github.com/ZerGo0/WireGuard-Allowed-IPs-Excluder) _(simplified by ChatGPT)_
To exclude a domain or IP address from routing through Wireguard:
```bash
wgdomain exclude /path/to/wireguard.conf example.com
```

### Resetting Settings
#### Accept All Domains
To reset the configuration to accept all domains:
```bash
wgdomain reset all /path/to/wireguard.conf
```

#### Exclude All Domains
To reset the configuration to exclude all domains:
```bash
wgdomain reset none /path/to/wireguard.conf
```

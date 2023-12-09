<div align="center">

# 🌐 Wireguard Domain Manager

![GitHub last commit](https://img.shields.io/github/last-commit/barabum0/wgdomain)
![GitHub issues](https://img.shields.io/github/issues/barabum0/wgdomain)
![GitHub stars](https://img.shields.io/github/stars/barabum0/wgdomain)
![License](https://img.shields.io/github/license/barabum0/wgdomain)

</div>

## 💡 About

Wireguard Domain Manager is a command-line tool for managing domains and IP addresses in Wireguard VPN configurations. It enables easy inclusion and exclusion of domains, as well as resetting settings for specific routing behaviors.

## 🛠 Installation

```bash
pipx install git+https://github.com/barabum0/wgdomain
wgdomain --help
```

## 📖 Usage

Examples of using commands:

### ➕ Adding a Domain

To add a domain or IP address for routing through Wireguard:

```bash
wgdomain include /path/to/wireguard.conf example.com
```

### ➖ Excluding a Domain

To exclude a domain or IP address from routing through Wireguard:

```bash
wgdomain exclude /path/to/wireguard.conf example.com
```

### 🔁 Resetting Settings

#### ✔️ Accept All Domains

To reset the configuration to accept all domains:

```bash
wgdomain reset all /path/to/wireguard.conf
```

#### ❌ Exclude All Domains

To reset the configuration to exclude all domains:

```bash
wgdomain reset none /path/to/wireguard.conf
```

## 🚑 Troubleshooting

For any issues or troubleshooting, please refer to the [GitHub Issues](https://github.com/barabum0/wgdomain/issues) section of the project.

## 🤝 Contribution

Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/barabum0/wgdomain/blob/main/LICENSE) file for details.

import ipaddress


def process_ip_networks(allowed_ips_str, disallowed_ips_str):
    def parse_ip_networks(ip_list_str):
        networks, invalid_ips = [], []
        for ip in ip_list_str.split(","):
            try:
                net = ipaddress.ip_network(ip.strip(), strict=False)
                networks.append(net)
            except ValueError:
                invalid_ips.append(ip.strip())
        return networks, invalid_ips

    def exclude_networks(allowed_networks, disallowed_networks):
        remaining_networks = set(allowed_networks)

        for disallowed in disallowed_networks:
            remaining_networks = {
                subnet for allowed in remaining_networks
                for subnet in allowed.address_exclude(disallowed) if allowed.overlaps(disallowed)
            } | {allowed for allowed in remaining_networks if not allowed.overlaps(disallowed)}

        return sorted(remaining_networks, key=lambda net: (net.version, net.network_address))

    allowed_networks, invalid_allowed = parse_ip_networks(allowed_ips_str)
    disallowed_networks, invalid_disallowed = parse_ip_networks(disallowed_ips_str)

    if invalid_allowed or invalid_disallowed:
        raise ValueError("Invalid IPs detected in inputs.")

    sorted_networks = exclude_networks(allowed_networks, disallowed_networks)
    return ", ".join(map(str, sorted_networks))

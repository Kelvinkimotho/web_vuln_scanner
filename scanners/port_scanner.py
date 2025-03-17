import nmap

def scan_ports(target):
    scanner = nmap.PortScanner()

    try:
        scanner.scan(target, arguments='-T4 -F')  # Faster scan with timing optimization
    except Exception as e:
        return {"error": f"Port scan failed: {str(e)}"}

    ports = {}
    for host in scanner.all_hosts():
        ports[host] = scanner[host]['tcp'] if 'tcp' in scanner[host] else {}

    return ports

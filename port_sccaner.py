import socket
import sys


def scan_ip(ip, start_port, end_port):
    print(f"starting scan on {ip}")
    tcp_scan(ip, start_port, end_port)
    print(f"finished scan on {ip}")


def scan_domain(domain, start_port, end_port):
    print(f"starting scan on {domain}")
    ip = socket.gethostbyname(domain)
    tcp_scan(ip, start_port, end_port)
    print(f"finished scan on {domain}")


def tcp_scan(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if not tcp.connect_ex((ip, port)):
                print(f"{ip}:{port}/TCP OPEN")
                tcp.close()
        except Exception as e:
            pass


if __name__ == "__main__":
    socket.setdefaulttimeout(1)

    if len(sys.argv) > 4:
        print("usage:  ./port_sccaner.py <ip> <start_port> <end_port>")
        print("usage:  ./port_sccaner.py <domain> <start_port> <end_port> -n")


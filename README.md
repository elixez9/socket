# Port Scanner — Simple TCP Port Scanner

A small, single-file Python TCP port scanner intended for learning and small-scale testing.  
This project demonstrates basic socket usage and port probing with `connect_ex()`.

> ⚠️ **Important**: Only use this tool on systems and networks you own or where you have explicit permission to test. Unauthorized scanning can be illegal and/or result in IP blocks.

---

## Features
- Scans a range of TCP ports on a given IP or hostname
- Default socket timeout (1 second) to avoid long waits
- Simple, human-readable output showing open ports
- No external dependencies — uses Python standard library

---

## Requirements
- Python 3.7+
- Standard library `socket`, `sys`, optionally `argparse` if you adopt suggested improvements

---

## Quick usage
```bash
# Basic
python3 port_scanner.py <ip_or_domain> <start_port> <end_port>

# Example
python3 port_scanner.py 192.168.1.10 20 1024

# With optional -n flag (implementation-defined behavior)
python3 port_scanner.py example.com 1 65535 -n

# Python Port Scanner

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)

A fast multithreaded TCP port scanner with service banner detection.

## Features
- Scans ports concurrently (50 threads)
- Detects service banners
- Saves results in JSON format
- Lightweight (no external dependencies)

## Usage
```bash
./port_scanner.py -t 192.168.1.1 -p 20-100 -o results.json
```

## Installation
```bash
git clone https://github.com/YOUR-USERNAME/python-port-scanner.git
cd python-port-scanner
chmod +x port_scanner.py
```

## Sample Output
```json
{
  "target": "192.168.1.1",
  "open_ports": [
    {"port": 22, "service": "SSH-2.0-OpenSSH"},
    {"port": 80, "service": "nginx/1.18.0"}
  ]
}
```

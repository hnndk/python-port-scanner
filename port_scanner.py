#!/usr/bin/env python3
#HNDKHNDKHNDKHNDKHNDKHNDKHNDKHNDKHNDKHNDKHNDKHNDKHNDKHNDK
import socket
import threading
import argparse
import json
from queue import Queue

print_lock = threading.Lock()
results = {"target": "", "open_ports": []}  

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        conn_result = sock.connect_ex((target, port))
        if conn_result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "Unknown"
            with print_lock:
                print(f"[+] Port {port} is open | Service: {banner}")
                results["open_ports"].append({"port": port, "service": banner})  # Store in list
        sock.close()
    except Exception as e:
        pass

def worker(target, queue):
    while not queue.empty():
        port = queue.get()
        scan_port(target, port)
        queue.task_done()

def main():
    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("-t", "--target", help="Target IP", required=True)
    parser.add_argument("-p", "--ports", help="Port range (e.g., 1-1000)", default="1-1000")
    parser.add_argument("-o", "--output", help="Save results to JSON file")
    args = parser.parse_args()

    target = args.target
    results["target"] = target  
    port_range = args.ports.split("-")
    start_port, end_port = int(port_range[0]), int(port_range[1])
    queue = Queue()

    print(f"\n[!] Scanning {target} (Ports: {start_port}-{end_port})...\n")
    for port in range(start_port, end_port + 1):
        queue.put(port)

    for _ in range(50):  
        t = threading.Thread(target=worker, args=(target, queue))
        t.daemon = True
        t.start()

    queue.join()

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=4)
        print(f"\n[+] Results saved to {args.output}")

if __name__ == "__main__":
    main()
#
#------------------------------####---------------------------------#
#                        EXECUTE WITH
#  ./port_scanner.py -t *TARGET IP* -p 1-1000 -o scan_results.json
#-----------------------------####----------------------------------#


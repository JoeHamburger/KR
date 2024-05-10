import socket
import threading
import os

def is_port_open(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            return True
    except (socket.timeout, ConnectionRefusedError):
        return False

def print_colored_block(is_open):
    if is_open:
        print("\033[92m", "█", "\033[0m", end="")
    else:
        print("\u001b[42m", "█", "\033[0m", end="")

def check_port(host, port):
    print_colored_block(is_port_open(host, port))

if __name__ == "__main__":
    host = "8.8.8.8"  # Google's public DNS server
    port_range_total = 100000
    for j in range(2, port_range_total // 5):
        for i in range(j * 5 - 5, j * 5):
            port_range = range(i - 5, i)
            threads = []
            for port in port_range:
                t = threading.Thread(target=check_port, args=(host, port))
                threads.append(t)
                t.start()
            for t in threads:
                t.join()
            print()
        os.system('clear')


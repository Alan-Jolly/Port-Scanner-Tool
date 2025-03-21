import socket
import threading

def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    result = scanner.connect_ex((ip, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    scanner.close()

def main():
    print("🔎 Simple Port Scanner Tool")
    target = input("Enter target IP address or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("\n✅ Scan complete!")

if __name__ == "__main__":
    main()

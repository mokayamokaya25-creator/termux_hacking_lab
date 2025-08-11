import socket

target = input("Enter target IP: ")
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

print(f"Scanning {target}...")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is open")
    s.close()

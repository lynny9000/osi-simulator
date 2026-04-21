import time
import re

# ===== Validation Functions =====
# These check user input before continuing

def validate_port(port):
    return port.isdigit() and 1 <= int(port) <= 65535

def validate_ip(ip):
    parts = ip.split(".")
    return (
        len(parts) == 4 and
        all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
    )

def validate_mac(mac):
    return re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", mac)

print()
print("=== Encapsulation (Building Packet) ===")
time.sleep(3)

# ===== Layer 7: Application =====
# Application creates the original data
print("\n--- Layer 7: Application ---")
data = input("Enter data (e.g. GET / HTTP/1.1): ") or "GET / HTTP/1.1"
print("Data:", data)

# Show starting packet
print("\nPacket so far:")
print(f"[DATA: {data}]")
print()
time.sleep(3)

# ===== Layer 4: Transport (TCP) =====
# TCP adds ports and wraps data
print("--- Layer 4: Transport (TCP) ---")

while True:
    source_port = input("Enter source port (default 12345): ") or "12345"
    if validate_port(source_port):
        source_port = int(source_port)
        break
    print("Invalid port. Must be 1–65535.\n")

while True:
    destination_port = input("Enter destination port (default 80): ") or "80"
    if validate_port(destination_port):
        destination_port = int(destination_port)
        break
    print("Invalid port. Must be 1–65535.\n")

tcp_segment = {
    "source_port": source_port,
    "destination_port": destination_port,
    "data": data
}

print("Source Port:", source_port)
print("Destination Port:", destination_port)
print("Payload:", data)

print("\nPacket so far:")
print(f"[TCP src={source_port} dst={destination_port}] -> "
      f"[DATA: {data}]")
print()
time.sleep(3)

# ===== Layer 3: Network (IP) =====
# IP adds logical addressing
print("--- Layer 3: Network (IP) ---")

while True:
    source_ip = input("Enter source IP (default 192.168.1.10): ") or "192.168.1.10"
    if validate_ip(source_ip):
        break
    print("Invalid IP format.\n")

while True:
    destination_ip = input("Enter destination IP (default 142.250.190.14): ") or "142.250.190.14"
    if validate_ip(destination_ip):
        break
    print("Invalid IP format.\n")

ip_packet = {
    "source_ip": source_ip,
    "destination_ip": destination_ip,
    "data": tcp_segment
}

print("Source IP:", source_ip)
print("Destination IP:", destination_ip)

print("\nPacket so far:")
print(f"[IP src={source_ip} dst={destination_ip}] -> "
      f"[TCP src={source_port} dst={destination_port}] -> "
      f"[DATA: {data}]")
print()
time.sleep(3)

# ===== Layer 2: Data Link (Ethernet) =====
# Ethernet adds MAC addresses
print("--- Layer 2: Data Link (Ethernet) ---")

while True:
    source_mac = input("Enter source MAC (default AA:BB:CC:DD:EE:01): ") or "AA:BB:CC:DD:EE:01"
    if validate_mac(source_mac):
        break
    print("Invalid MAC format (XX:XX:XX:XX:XX:XX).\n")

while True:
    destination_mac = input("Enter destination MAC (default FF:EE:DD:CC:BB:AA): ") or "FF:EE:DD:CC:BB:AA"
    if validate_mac(destination_mac):
        break
    print("Invalid MAC format (XX:XX:XX:XX:XX:XX).\n")

ethernet_frame = {
    "source_mac": source_mac,
    "destination_mac": destination_mac,
    "data": ip_packet
}

print("Source MAC:", source_mac)
print("Destination MAC:", destination_mac)

print("\nPacket so far:")
print(f"[ETH src={source_mac} dst={destination_mac}] -> "
      f"[IP src={source_ip} dst={destination_ip}] -> "
      f"[TCP src={source_port} dst={destination_port}] -> "
      f"[DATA: {data}]")
print()
time.sleep(3)

# ===== Transmission =====
# Simulate sending across the network
print("--- Data transmitted over network ---\n")
time.sleep(3)

# ======================
# DECAPSULATION
# ======================
# Receiving side unwraps layers

print("=== Decapsulation (Receiving Data) ===\n")
time.sleep(3)

# ===== Layer 2 =====
print("--- Layer 2: Data Link (Ethernet) ---")
print("Source MAC:", ethernet_frame["source_mac"])
print("Destination MAC:", ethernet_frame["destination_mac"])

ip_payload = ethernet_frame["data"]

print("\nPacket now:")
print(f"[IP src={source_ip} dst={destination_ip}] -> "
      f"[TCP src={source_port} dst={destination_port}] -> "
      f"[DATA: {data}]")
print()
time.sleep(3)

# ===== Layer 3 =====
print("--- Layer 3: Network (IP) ---")
print("Source IP:", ip_payload["source_ip"])
print("Destination IP:", ip_payload["destination_ip"])

tcp_payload = ip_payload["data"]

print("\nPacket now:")
print(f"[TCP src={source_port} dst={destination_port}] -> "
      f"[DATA: {data}]")
print()
time.sleep(3)

# ===== Layer 4 =====
print("--- Layer 4: Transport (TCP) ---")
print("Source Port:", tcp_payload["source_port"])
print("Destination Port:", tcp_payload["destination_port"])

app_data = tcp_payload["data"]

print("\nPacket now:")
print(f"[DATA: {data}]")
print()
time.sleep(3)

# ===== Layer 7 =====
print("--- Layer 7: Application ---")
print("Data:", app_data)
print()
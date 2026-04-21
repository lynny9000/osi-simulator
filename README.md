# OSI Encapsulation Simulator

A Python-based OSI model simulator that demonstrates encapsulation and decapsulation of data through network layers.

## Features

* Step-by-step packet creation (Application - TCP - IP - Ethernet)
* Step-by-step packet breakdown (Ethernet - IP - TCP - Application)
* User input at each layer
* Displays packet structure as it builds and shrinks
* Input validation for ports, IP addresses, and MAC addresses

## How it works

The script simulates how data moves through the OSI layers:

* Application layer creates data
* Transport layer adds TCP ports
* Network layer adds IP addresses
* Data Link layer adds MAC addresses

The packet is then “sent” and unpacked in reverse order on the receiving side.

## Usage

Run:

python osi_simulator.py

Example:

Enter data (e.g. GET / HTTP/1.1): GET / HTTP/1.1
Enter source port (default 12345): 12345
Enter destination port (default 80): 80
Enter source IP (default 192.168.1.10): 192.168.1.10
Enter destination IP (default 142.250.190.14): 142.250.190.14

Output:
=== Encapsulation (Building Packet) ===

--- Layer 7: Application ---
Data: GET / HTTP/1.1

Packet so far:
[DATA: GET / HTTP/1.1]

--- Layer 4: Transport (TCP) ---
Source Port: 12345
Destination Port: 80
Payload: GET / HTTP/1.1

Packet so far:
[TCP src=12345 dst=80] -> [DATA: GET / HTTP/1.1]

--- Layer 3: Network (IP) ---
Source IP: 192.168.1.10
Destination IP: 142.250.190.14

Packet so far:
[IP src=192.168.1.10 dst=142.250.190.14] -> [TCP src=12345 dst=80] -> [DATA: GET / HTTP/1.1]

--- Layer 2: Data Link (Ethernet) ---
Source MAC: AA:BB:CC:DD:EE:01
Destination MAC: FF:EE:DD:CC:BB:AA

Packet so far:
[ETH src=AA:BB:CC:DD:EE:01 dst=FF:EE:DD:CC:BB:AA] -> [IP src=192.168.1.10 dst=142.250.190.14] -> [TCP src=12345 dst=80] -> [DATA: GET / HTTP/1.1]

--- Data transmitted over network ---

...

## Notes

* Demonstrates OSI layers (2, 3, 4, 7)
* Includes basic input validation

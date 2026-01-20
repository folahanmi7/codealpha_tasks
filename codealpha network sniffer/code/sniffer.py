from scapy.all import sniff

def capture_packet(packet):
    print(packet.summary())

print("Starting network sniffer...")
sniff(prn=capture_packet, count=20)
print("Sniffing finished.")

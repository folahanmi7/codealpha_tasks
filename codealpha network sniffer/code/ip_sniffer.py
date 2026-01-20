from scapy.all import sniff, IP

def packet_callback(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        print(f"Source: {src} → Destination: {dst}")

sniff(count=20, prn=packet_callback)

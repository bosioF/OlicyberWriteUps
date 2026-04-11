from scapy.all import rdpcap, IP

IPs = {"172.19.0.2", "172.67.157.96"}
packets = rdpcap("llt.pcap")

flag = ""
for packet in packets:
    if IP in packet:
        if packet[IP].src in IPs and packet[IP].dst in IPs:
            flag += chr(packet[IP].ttl)
            
print(flag.replace("?", "").replace("@", ""))
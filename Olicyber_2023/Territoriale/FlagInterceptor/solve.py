import pyshark
from collections import defaultdict

streams = defaultdict(str)

cap = pyshark.FileCapture('flag-interceptor.pcap')

for p in cap:
    if 'data' in p:
        ip = p.ip.src
        data = p.data.data
        streams[ip] += bytes.fromhex(data).decode()[:-1]

for addr in streams:
    stream = streams[addr]
    if stream.startswith('flag{') and stream.endswith('}'):
        print(stream)
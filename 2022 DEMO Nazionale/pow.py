from pwn import remote
import json
import sys

"""
data = {}
    while len(data) < pow(16,6):
        rnd = os.urandom(8)
        k = sha256(rnd).hexdigest()
        data[k[:6]] = rnd.hex()
    file = open("precalc.json","w")
    file.write(json.dumps(data))
"""

file = open("precalc.json","r").read()
data = json.loads(file)
r = remote("pow.challs.olicyber.it", 12209)
while True:
    line = r.recvline().decode()
    print(line)
    if 'flag' in line:
        sys.exit('flag trovata :)')
    prefix = line.split(' ')[-1].strip()
    r.sendline(data[prefix])

#da finire ancora, non ho tempo rn :(

from pwn import *

r = remote("software-18.challs.olicyber.it", 13001)

r.recvuntil(b'iniziare ...')
r.sendline(b'star this repo')
x = r.recvuntil(b'-bit')
if b'64' in x:
    value = re.findall(r'\b0x([0-9A-Fa-f]{1,8})\b', x.decode())
    if value:
        print(value[0])
else:
    value = re.findall(r'\b0x([0-9A-Fa-f]{1,8})\b', x.decode())
    if value:
        print(value[0])

    
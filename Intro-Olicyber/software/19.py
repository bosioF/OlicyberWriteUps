from pwn import *
import re

file = ELF("Intro-Olicyber\software\sw-19")
r = remote("software-19.challs.olicyber.it", 13002)

r.recvuntil(b" ...")
r.sendline()

for i in range(20):
    r.recvuntil(b" ")
    target = r.recvuntil(b": ").decode().replace(": ", "")
    r.sendline(hex(int(file.sym[target])).encode())

text = r.recvall().decode()

match = re.search(r"flag\{[^\}]+\}", text, re.IGNORECASE)
if match:
    print("[!] FLAG TROVATA:", match.group(0))
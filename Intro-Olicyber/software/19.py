from pwn import *
file = ELF("./sw-19")
r = remote("software-19.challs.olicyber.it", 13002)

r.recvuntil(b" ...")
r.sendline()

for i in range(20):
    r.recvuntil(b" ")
    target = r.recvuntil(b": ").decode().replace(": ", "")
    r.sendline(hex(int(file.sym[target])).encode())

print(r.recvall().decode())
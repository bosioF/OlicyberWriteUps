from pwn import *

HOST = "spg.challs.olicyber.it"
PORT = int(38052)

payload = b"gabibbo;index0=0;index1=1;index2=2;index3=3;a=donpollo\x01"

r = remote(HOST, PORT)

r.sendlineafter(b"> ", b"1")
r.sendlineafter(b"? ", b"gabibbo")
r.sendlineafter(b"> ", b"1")
r.sendlineafter(b"? ", payload)
r.recvline()
token = r.recvline().decode().split(": ")[1][:5*32]
r.sendlineafter(b"> ", b"2")
r.sendlineafter(b"? ", token.encode())
flag = r.recvline().decode().split()[-1].replace("-", "")
print(flag)
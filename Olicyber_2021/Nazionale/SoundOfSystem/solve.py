from pwn import *

HOST = 'soundofsystem.challs.olicyber.it'
PORT = 15000

r = remote(HOST, PORT)

def pad(m):
    if len(m)%48 == 0:
        return m
    return m + bytes([48-len(m)%48])*(48-len(m)%48)

padded = pad(b"show_flag")
payload = padded[16:32]+padded[:16]+padded[32:]

r.recvuntil(b"> ")
r.sendline(payload)
r.interactive()

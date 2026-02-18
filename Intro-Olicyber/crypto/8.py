#I can't figure out why it doesn't always work, try until it works ig lol
from pwn import *

HOST = "crypto-08.challs.olicyber.it"
PORT = 30001

conn = remote(HOST, PORT)
conn.recvuntil(b'\n\n')
eq = conn.recvuntil(b'=').decode().strip().replace(" =", "").split(" ")
t = []
for i in eq:
    if i != '%':
        t.append(int(i))

conn.sendline(f"{t[0]%t[1]}".encode())

conn.recvuntil(b'\n\n')
conn.recvuntil(b'\n\n')
resp = conn.recvuntil(b'no) ').decode().strip().replace(" ==", "").replace("(mod", "").replace("(si/no)", "").replace(")?", "").split(" ")
for i in resp:
    if i != '':
        t.append(int(i))

if (int(t[0]) - int(t[1])) % int(t[3]) == 0:
    conn.sendline(b"si")
else:
    conn.sendline(b"no")

flag = conn.recvuntil(b"}\n").decode().strip().replace("Corretto!", "").replace("Grande!", "")
print(flag)
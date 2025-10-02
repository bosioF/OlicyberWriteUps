from pwn import *

url = "software-17.challs.olicyber.it"
port = 13000

r = remote(url, port)
r.recv()
r.sendline(b's')

for i in range(10):
    r.recvuntil(b'numeri\n[').decode()
    list = r.recvuntil(b']').decode()[:-1]
    list = list.split(', ')

    tot = 0
    for e in list:
        tot += int(float(e))

    r.recv()
    tot = str(tot)
    r.sendline(tot.encode())
    if i is not 9:
        giusto = r.recvuntil(b'questi')
    else: 
        giusto = r.recv()
    print(giusto.decode())

r.close()
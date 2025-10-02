from pwn import *

connection = remote("software-18.challs.olicyber.it", 13001)

def prendiUltimi():
    for i in range(1, 102):
        if i < 100:
            r = connection.recvline().decode()[27:-1]
        else:
            r = connection.recvline().decode()[28:-1]

        r = r.split(' packed a ')
        
        if r[i] == "64-bit":
            packed = p64(int(r[0], base=16))
        else:
            packed = p32(int(r[0], base=16))
        
        r = connection.recvuntil(b'[+] Result : ')
        connection.send(packed)

connection.recv()
connection.sendline(b'e')

prendiUltimi()

connection.close()
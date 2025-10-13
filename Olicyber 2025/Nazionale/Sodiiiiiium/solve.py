import hashlib

# valore recuperato dal data dump usato nella funzione sodium_memcmp()
target = bytes.fromhex("...") 

hash_str = b"tung tung tung sahur VS cappuccino assassino"
hash_result = hashlib.sha512(hash_str).digest()

buf = bytearray(0x40)
for i in range(0x40):
    buf[i] = target[i] ^ hash_result[i]

for i in range(0, 0x40, 2):
    buf[i] ^= 0x20

print("Input corretto:", buf.decode())

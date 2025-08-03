import random
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import long_to_bytes


flag = open('flag.txt', 'rb').read()

g = 2

print(f'{g = }')

a = random.randint(2, 2**12 - 2)
b = random.randint(2, 2**12 - 2)

A = pow(g, a)
B = pow(g, b)

print(f'{A = }')
print(f'{B = }')

K = pow(A, b)


key = hashlib.sha256(long_to_bytes(K)).digest()

enc = AES.new(key, AES.MODE_ECB).encrypt(pad(flag, AES.block_size)).hex()
print(f'{enc = }')
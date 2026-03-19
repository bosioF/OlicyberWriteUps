from Crypto import *
import re
from sympy import mod_inverse
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import unpad

p = 19732127739520259389
q = 22432345460202197593
e = 65537

n = p*q
print(n)
phiN = (p-1)*(q-1)
print(phiN)
d = mod_inverse(e, phiN)
print(d)
r = bytes_to_long(b'CINI')
print(pow(r, e, p*q))
chiave = pow(bytes_to_long(bytes.fromhex("40408b8607f7d14d2de271f2eccc7b86")), d, p*q)
a = AES.new(long_to_bytes(chiave), AES.MODE_CBC, iv=bytes.fromhex("312e18c3b6590ca5e9562ca14dc18c39"))
flag = (unpad(a.decrypt(bytes.fromhex("e526db767b72ab76dea7ca7d7056c19707092d80a2cba9ac341511f6f1efea75")), AES.block_size))
print(flag.decode())
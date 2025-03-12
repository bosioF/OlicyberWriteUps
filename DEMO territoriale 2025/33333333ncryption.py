flag = b"flag{REDACTED}"

ROUNDS = 5
def encrypt(flag):
    enc = flag
    for _ in range(ROUNDS):
        enc = enc.hex()[::-1].encode()
    
    return enc.hex()

print(encrypt(flag))
import string

ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"

cipher_bytes = bytes.fromhex(ciphertext)

for key in range(256):
    plaintext_bytes = bytes([b ^ key for b in cipher_bytes])

    try:
        if all(chr(x) in string.printable for x in plaintext_bytes):
            plaintext = plaintext_bytes.decode('utf-8')
            if b"_" in plaintext_bytes:
                print(f"Chiave: {key:02x}, Testo decifrato: {plaintext}")
    except UnicodeDecodeError:
        pass

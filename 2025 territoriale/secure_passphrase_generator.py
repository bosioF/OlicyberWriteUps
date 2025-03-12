from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Token cifrato in esadecimale
enc_token = "784f623981f52701fe566742e81c042cd6ce5dc4e26a56c95b9ed2a30c0fe7c4f2161023d2115c73f47191e4af7fa841de94c44781b37f09eff0325aa613a203b642e75824b15fe1a44aaa499c0fbdf2"

# Converti il token in bytes
enc_token_bytes = bytes.fromhex(enc_token)

# Estrai IV (primi 16 byte) e ciphertext (il resto)
iv = enc_token_bytes[:16]
ciphertext = enc_token_bytes[16:]

# Chiave AES (devi conoscere la chiave usata dal server)
# Nel codice originale, la chiave è generata casualmente con `os.urandom(16)`
# Se non hai la chiave, non puoi decifrare il token direttamente.
# Supponiamo che tu abbia ottenuto la chiave in qualche modo (ad esempio, attraverso un'altra vulnerabilità).
key = b"supersecretkey123"  # Sostituisci con la chiave corretta

# Decifra il token
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(ciphertext), 16).decode('utf-8')

# Stampa il token decifrato
print(f"Token decifrato: {decrypted}")
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

token_hex = "5b3ac6e9623c804254dedc0dc27939379e40f7a865e0ef56194f56aa6b5630fe3988b3ccd4aa8e935cb4e68a1be0621f0d663e8ca8dbd18fa02687770c8de7648f97eca3508013a7334cf7540bfa2e42"

enc_token = binascii.unhexlify(token_hex)
iv = enc_token[:16]
ciphertext = enc_token[16:]

key = b'\x8a\xd7\xe3\xfd\x01y\xef^J/\xd2\x08\xb1\xb0\xa3\xed'

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = cipher.decrypt(ciphertext)

try:
    decrypted_data = unpad(decrypted, 16)
    print(decrypted_data.decode('utf-8'))
except ValueError as e:
    print("Errore di padding:", e)
    print("Dati decriptati senza rimozione del padding (in esadecimale):")
    print(decrypted.hex())

from Crypto.Cipher import AES
import binascii

key = bytes.fromhex('211a7c95cbe4e164ba76728089b0437a')
ciphertext = bytes.fromhex('3117480c68426be9b7de1253d7f69eada96ef14b04491d4170dc9a8e6553e2ba')
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)
print(plaintext.decode('utf-8'))

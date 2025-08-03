from Crypto.Hash import HMAC,SHA3_384,SHA224

msg = 'hash_me_pls'
msgBytes = msg.encode()

hash_obj = SHA3_384.new(msgBytes)
hash_hex = hash_obj.hexdigest()

print(hash_hex)

hex_key = 'bb5a1a8474c726d4ddb307bc8b6e06c9297d4fec3b4e9b1ce1e1edae0f249f5f'
msg1 = 'La mia integrità è importante!'

key = bytes.fromhex(hex_key)
msgBytes1 = msg1.encode()
hmac_obj = HMAC.new(key, msgBytes1, SHA224)
hmac_hex = hmac_obj.hexdigest()

print(hmac_hex)



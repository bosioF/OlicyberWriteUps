"""import hashlib
import string

def find_input():
    characters = string.ascii_letters + string.digits
    max_len = 6

    from itertools import product

    for length in range(1, max_len + 1):
        for combo in product(characters, repeat=length):
            input_str = ''.join(combo)
            hash_val = hashlib.md5(input_str.encode()).hexdigest()
            if hash_val[:24] == input_str:
                return input_str
    return None

input_trovato = find_input()
if input_trovato:
    print(f"Input trovato: {input_trovato}")
else:
    print("Nessun input valido trovato.")
"""
import hashlib

def try_input():
    for i in range(1000000):
        user_input = str(i)
        md5_hash = hashlib.md5(user_input.encode()).hexdigest()

        if md5_hash[:24] == user_input:
            print(f"Trovato input: {user_input}")
            return user_input
    return None


user_input = try_input()
if user_input:
    print(f"Input valido trovato: {user_input}")
else:
    print("Nessun input valido trovato.")

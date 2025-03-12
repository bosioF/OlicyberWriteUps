import hashlib

def find_magic_hash():
    prefix = '0e'
    for i in range(10**22):
        s = prefix + str(i).zfill(22)
        md5 = hashlib.md5(s.encode()).hexdigest()
        if md5[:24].startswith(prefix) and md5[2:24].isdigit():
            print(f"Found: {s}")
            return s
    return None

find_magic_hash()

""""
#0e215962017
import hmac
import hashlib

import requests

url = f'http://confuse-me.challs.olicyber.it/?input='
def brute_force_hash():
    for i in range(200000000, 500000000):
        prefix = '0e'
        hash = prefix + str(i)
        print(hash)
        r = requests.get(url + str(hash))
        #print(r.text)
        if r.text.__contains__("flag"):
            print(r.text)
            break

    print("Nessun valore trovato.")
    return None


brute_force_hash()
"""
"""import hmac
import hashlib
def find_valid_number():
    for i in range(1, 1835970773):
        print(i)
        out = hmac.new(b'', f'admin|{i}'.encode(), hashlib.md5).hexdigest()

        if out.startswith('0e'):
            try:
                if int(out) == 0:  # Verifica se PHP valuterebbe questa stringa come 0
                    print(f"Trovato: {i} - {out}")
                    break
            except ValueError:
                pass  # Se la conversione fallisce, continua il ciclo


find_valid_number()


import hashlib

def find_valid_input():
    attempts = 0
    while True:
        user_input = str(attempts)

        md5_hash = hashlib.md5(user_input.encode()).hexdigest()
        # Verifica se l'input è uguale ai primi 24 caratteri dell'hash
        if user_input == md5_hash[:24]:
            return user_input, md5_hash

        attempts += 1

        if attempts % 1000000 == 0:
            print(f"Tentativi: {attempts}")

solution, hash_result = find_valid_input()
print(f"Trovato! Input valido: {solution}")
print(f"Hash corrispondente: {hash_result}")


import hashlib
import string
import random


# Funzione per generare stringhe casuali
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def find_magic_hash():
    attempts = 0
    while True:
        user_input = str(attempts)

        md5_hash = hashlib.md5(user_input.encode()).hexdigest()

        if md5_hash.startswith("0e") and md5_hash[2:].isdigit():
            return user_input, md5_hash

        attempts += 1

        if attempts % 1000000 == 0:
            print(f"Tentativi: {attempts}")


solution, hash_result = find_magic_hash()
print(f"Trovato! Input: {solution}")
print(f"Hash MD5: {hash_result}")

import hashlib
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def find_collision():
    while True:
        user_input = generate_random_string(24)
        md5_hash = hashlib.md5(user_input.encode()).hexdigest()
        print(user_input)
        if user_input == md5_hash[:24]:
            print(f"Collision found: {user_input}")
            return user_input

collision = find_collision()
print(f"Use the following input to get the flag: {collision}")


import hashlib
import re
import requests
import itertools

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def brute_force():
    for lunghezza in range(1, 10):
        for comb in itertools.product(alfabeto, repeat=lunghezza):
            parola = ''.join(comb)
            md5_hash = hashlib.md5(parola.encode()).hexdigest()

            if parola == md5_hash[:24]:
                print(f"Trovato match: {parola}")
                return parola
    print("Nessun match trovato")
    return None

brute_force()
"""

"""
url = 'http://confuse-me.challs.olicyber.it/'
x = 0

for i in range(1000000000000):
    x += 1
    print(x)
    value = str(i)
    md5_hash = hashlib.md5(value.encode()).hexdigest()

    if md5_hash.startswith('0e') and md5_hash[2:].isdigit():
        print(f"Trovato input valido: {value}, Hash: {md5_hash}")
        r = requests.post(url, data={'input': value})
        print(r.text)
        break

    #if re.match(r'^0e\d+$', md5_hash):
        #print(f"Trovato! Input: {value}, Hash: {md5_hash}")
        #break
"""
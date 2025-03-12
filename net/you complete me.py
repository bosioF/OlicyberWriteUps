"""
#from secret import key
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os


def decrypt_char(char):
    # l'input dell'utente è un carattere ASCII cifrato.
    # qui lo decifriamo e verifichiamo che effettivamente sia solo un carattere
    ch = unpad(aes.decrypt(bytes.fromhex(char)), BLOCK_LENGTH)
    assert(len(ch) == 1)
    return ch


def next_char(char):
    return (ord(char) + 1).to_bytes(1, 'big')


def get_words_by_prefix(prefix):
    # estraggo l'ultimo carattere del prefisso
    prefix, last_char = prefix[:-1], prefix[-1].to_bytes(1, 'big')

    # esempio: se il prefisso è mal allora voglio tutte le parole W tali per cui mal <= W < mam
    # quindi lower_bound = mal e upper_bound = mam
    lower_bound = prefix + last_char
    upper_bound = prefix + next_char(last_char)

    return [w for w in words if lower_bound <= w < upper_bound]

def handle():
    curr_prefix = b''
    while True:
        # l'input del client è un singolo carattere cifrato
        char = input()
        curr_prefix += decrypt_char(char)

        words = [encrypt_word(w) for w in get_words_by_prefix(curr_prefix)]
        print('\n'.join(words))
        print('end')


if __name__ == "__main__":
    handle()

#decrypt_char('ba230ba2c')
#print(ch)
"""

with open('words.txt', 'r') as file:
    contenuto = file.read()
    parole = contenuto.split()
    for parola in parole:
        if len(parola) == 13 and parola[4] == parola[5] and parola[3] == parola[7] == parola[11]:
            print(parola)


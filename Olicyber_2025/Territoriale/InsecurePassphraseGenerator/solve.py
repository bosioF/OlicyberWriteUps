import string

words = [
    "casa", "albero", "notte", "sole", "montagna", "fiume", "mare", "vento", "nuvola",
    "pioggia", "strada", "amico", "sorriso", "viaggio", "tempo", "cuore", "stella",
    "sogno", "giorno", "libro", "porta", "luce", "ombra", "silenzio", "fiore", "luna"
]

inverse_map = {word: chr(idx + ord('a')) for idx, word in enumerate(words)}

ciphered_passphrase = "fiume-amico-casa-mare-{-amico-tempo-viaggio-mare-_-sole-tempo-montagna-giorno-viaggio-libro-_-sorriso-montagna-casa-viaggio-_-giorno-montagna-notte-porta-sogno-montagna-_-luce-nuvola-giorno-stella-luce-cuore-casa-libro-}"

parts = ciphered_passphrase.split('-')

decoded_flag = []
for part in parts:
    if part in inverse_map:
        decoded_flag.append(inverse_map[part]) 
    else:
        decoded_flag.append(part)  

print(''.join(decoded_flag))

import string

# Lista delle parole usate per la mappatura
words = [
    "casa", "albero", "notte", "sole", "montagna", "fiume", "mare", "vento", "nuvola",
    "pioggia", "strada", "amico", "sorriso", "viaggio", "tempo", "cuore", "stella",
    "sogno", "giorno", "libro", "porta", "luce", "ombra", "silenzio", "fiore", "luna"
]

# Costruzione della tabella inversa
inverse_map = {word: chr(idx + ord('a')) for idx, word in enumerate(words)}

# Passphrase cifrata
ciphered_passphrase = "fiume-amico-casa-mare-{-amico-tempo-viaggio-mare-_-sole-tempo-montagna-giorno-viaggio-libro-_-sorriso-montagna-casa-viaggio-_-giorno-montagna-notte-porta-sogno-montagna-_-luce-nuvola-giorno-stella-luce-cuore-casa-libro-}"

# Dividi la passphrase in parti
parts = ciphered_passphrase.split('-')

# Decodifica
decoded_flag = []
for part in parts:
    if part in inverse_map:
        decoded_flag.append(inverse_map[part])  # Sostituisci con la lettera
    else:
        decoded_flag.append(part)  # Copia caratteri non mappati

# Unisci per ottenere il flag
decoded_flag = ''.join(decoded_flag)
print(f"Flag decodificato: {decoded_flag}")

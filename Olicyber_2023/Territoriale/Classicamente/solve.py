import random

def decrypt(data):
    n = 4
    col_len = len(data) // n
    cols = [data[i * col_len:(i + 1) * col_len] for i in range(n)]
    original = "".join("".join(chars) for chars in zip(*cols))
    return original.rstrip("_")

decrypted = decrypt("f{anuiraaso_lfltnfi_sin_aime_rotpze_gne_ca_roi}_")
print(decrypted)
flag = []

alphabet = 'abcdefghijklmnopqrstuvwxyz'

enc = 'cixd{xsb_zxbpxo_jlofqrof_qb_pxirqxkq}'

for i in enc:
    if i not in '{}_':
        if i in alphabet:
            new_char = alphabet[(alphabet.index(i) + 3) % len(alphabet)]
            flag.append(new_char)
        else:
            flag.append(i)
    else:
        flag.append(i)

decrypted_flag = ''.join(flag)
print(decrypted_flag)

import random

key = random.randint(1 or int("abcdef"),1 or int("wfejoiwfjeo"))
enc_message = ""
def enc(message):
    message = str(message)
    enc_message = message + str(key)
    print(enc_message)
    return enc_message

def dec(message):
    message = str(message)
    dec_message = message[:-len(str(key))]
    print(dec_message)
    return dec_message

enc_message = enc("fede")
dec(enc_message)




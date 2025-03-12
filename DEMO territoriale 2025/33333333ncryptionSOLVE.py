ROUNDS = 5


def decrypt(enc):
    enc = bytes.fromhex(enc)
    for _ in range(ROUNDS):
        enc = enc.decode()[::-1]
        enc = bytes.fromhex(enc)

    return enc

encrypted_flag = "3333363333333333333334333333333333333333333333333333373333333333333336333333333333333533333333333333333333333333333336333333333333333333333333333333303333333333333333333333333333333333333333333333333333333333333331333333333333333333333333333333333333333333333333333333333333333433333333333333333333333333333337333333333333333333333333333333303333333333333333333333333333333733333333333333333333333333333339333333333333333333333333333333373333333333333333333333333333333233333333333333333333333333333337333333333333333333333333333333333333333333333333333333333333333633333333333333363333333333333335333333333333333333333333333333363333333333333333333333333333333333333333333333333333333333333333333333333333333633333333333333363333333333333333333333333333333533333333333333333333333333333334333333333333333333333333333333373333333333333333333333333333333033333333333333333333333333333333333333333333333633333333333333353333333333333333333333333333333633333333333333363333333333333336333333333333333333333333333333353333333333333333333333333333333333333333333333333333333333333337333333333333333333333333333333313333333333333333333333333333333333333333333333363333333333333336333333333333333333333333333333353333333333333333333333333333333733333333333333333333333333333336333333333333333633333333333333353333333333333333333333333333333633333333333333333333333333333331333333333333333333333333333333333333333333333333333333333333333433333333333333333333333333333336333333333333333333333333333333303333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333363333333333333336333333333333333533333333333333333333333333333336333333333333333333333333333333333333333333333333333333333333333333333333333333363333333333333336333333333333333333333333333333353333333333333336333333333333333533333333333333333333333333333336333333333333333333333333333333313333333333333333333333333333333333333333333333333333333333333334333333333333333333333333333333333333333333333333333333333333333733333333333333333333333333333336333333333333333333333333333333343333333333333333333333333333333333333333333333363333333333333336333333333333333333333333333333353333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333633333333333333363333333333333335333333333333333333333333333333363333333333333333333333333333333033333333333333333333333333333333333333333333333633333333333333323333333333333333333333333333333733333333333333333333333333333337333333333333333333333333333333363333333333333333333333333333333133333333333333333333333333333336333333333333333633333333333333333333333333333333333333333333333633333333333333333333333333333336333333333333333333333333333333363333333333"
original_flag = decrypt(encrypted_flag)
print(original_flag.decode())

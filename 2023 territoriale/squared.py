from random import randint
from hashlib import sha256
from Crypto.Util.number import long_to_bytes, bytes_to_long

class CramerShoup:
    def __init__(self):
        q = 11470138098838773708030299067136047693985643409815055516364871317327807079521448915691685861415122090973650886160077675041872096255748644205171133021906581
        g1 = q * randint(1, q//2) + 1
        g2 = q * randint(1, q//2) + 1
        assert g1 != g2
        self.params = (q, g1, g2)
        self.pubkey = None
        self.privkey = None

    def get_params(self):
        return self.params

    def gen_keypair(self):
        q, g1, g2 = self.params
        x1 = randint(1, q-1)
        x2 = randint(1, q-1)
        y1 = randint(1, q-1)
        y2 = randint(1, q-1)
        z = randint(1, q-1)

        c = (pow(g1, x1, q**2)*pow(g2, x2, q**2)) % q**2
        d = (pow(g1, y1, q**2)*pow(g2, y2, q**2)) % q**2
        h = pow(g1, z, q**2)

        self.pubkey = (c, d, h)
        self.privkey = (x1, x2, y1, y2, z)

        return self.pubkey, self.privkey

    def import_key(self, pubkey, privkey = None):
        self.pubkey = pubkey
        self.privkey = privkey

    def encrypt(self, message):
        if self.pubkey == None:
            return None

        m = bytes_to_long(message)
        q, g1, g2 = self.params
        k = randint(1, q-1)
        u1 = pow(g1, k, q**2)
        u2 = pow(g2, k, q**2)
        e = (pow(self.pubkey[-1], k, q**2) * m) % q**2
        a = sha256(str(u1*u2*e).encode()).digest()
        v = (pow(self.pubkey[0], k, q**2) * pow(self.pubkey[1], k*bytes_to_long(a), q**2)) % q**2

        return (u1, u2, e, v)

    def decrypt(self, message): # TODO
        pass

flag = open("../flags.txt", "rb").read().strip()
cipher = CramerShoup()
params = cipher.get_params()
pubkey, _ = cipher.gen_keypair()

enc_flag = cipher.encrypt(flag)

print(params)
print(pubkey)
print(enc_flag)
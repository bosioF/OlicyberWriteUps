from math import gcd

#a = w, b = k, trova x,y tali che x*a + y*b == GCD(a,b)
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # GCD, x, y
    gcd1, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


a = 102 
b = 91
gcd1, x, y = extended_gcd(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"x = {x}, y = {y}")

#a è invertibile mod mod? (si/no) 
a = 102
mod = 91

if gcd(a, mod) == 1:
    print("Sì, 102 è invertibile modulo 91.")
else:
    print("No, 102 non è invertibile modulo 91.")
    
    
def mod_inverse(a, m):
    # Algoritmo esteso di Euclide
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0  # gcd, x, y
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverso non esiste
    else:
        return x % m

#Qual è l'inverso di a modulo mod?
# Esempio
a = 23
mod = 82
inverse = mod_inverse(a, mod)

if inverse is not None:
    print(f"L'inverso di {a} modulo {mod} è {inverse}.")
else:
    print(f"{a} non ha un inverso modulo {mod}.")


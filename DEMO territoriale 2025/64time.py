def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # GCD, x, y
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

print("a?")
a = input()
print("b?")
b = input()
gcd, x, y = extended_gcd(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"x = {x}, y = {y}")


numbers = [23, 31, 43, 47, 83, 71, 19, 23, 43, 17, 67, 37, 23, 31, 11, 7, 71, 41, 13]

def generate_primes(limit):
    primes = []
    candidate = 2
    while len(primes) < limit:
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

max_number = max(numbers)
primes = generate_primes(100)
prime_list = [p for p in primes if p <= max_number]

result = []
for num in numbers:
    if num in prime_list:
        position = prime_list.index(num) + 1
        result.append(chr(64 + position))

decoded_message = "".join(result)
print(f"Decoded Message: flag{{{decoded_message}}}")


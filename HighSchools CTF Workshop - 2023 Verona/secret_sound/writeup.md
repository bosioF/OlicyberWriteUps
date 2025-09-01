# Prime Numbers Encoding Challenge – Writeup

## Challenge Description
We are given a sequence of numbers. The goal is to interpret them using their positions in the ordered list of prime numbers and then reconstruct the hidden flag.

## Exploit
```python
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
print(f"flag{{{decoded_message}}}")
````

## Code Analysis

1. **Input Data**
   The challenge provides a list of numbers, all of which are prime.

2. **Prime Generation**

   * The function `generate_primes(limit)` builds a list of the first 100 prime numbers.
   * From this, a `prime_list` is created containing all primes less than or equal to the maximum value in `numbers`.

3. **Mapping Numbers to Letters**

   * For each number in the sequence, the script finds its **index in the prime list**.
   * Since indexing starts at `0`, `+1` is added to get the correct position.
   * Each position is mapped to a letter using `chr(64 + position)` (`A=1`, `B=2`, …).

4. **Reconstructing the Flag**

   * All mapped characters are concatenated into `decoded_message`.
   * The final output is printed in the format:

     ```
     flag{<decoded_message>}
     ```

## Exploitation Steps

1. Generate a list of prime numbers up to the maximum in the input.
2. Determine each input number’s position in the prime list.
3. Convert positions into letters (`A=1, B=2, ...`).
4. Concatenate letters into the final flag string.

## Solution

Running the exploit reveals the decoded flag:

```
flag{IKNOWTHINGSLIKEDTMF}
```

## Key Takeaway

This challenge demonstrates a **number-to-letter encoding** scheme based on prime indices. Recognizing the relationship between the input numbers and their positions in the prime sequence is key to solving it.
# XOR Decryption Challenge – Writeup

## Challenge Description
We are given a ciphertext encoded in hexadecimal form. The challenge hints at using a key (`gabibbo`) to decrypt it. Our goal is to recover the plaintext message.

## Exploit
```python
testo_hex = "2e35233a272114063e1a06103d0d3804131c030e1c38150d36013d0202000c1a3d01301f0e1036003d0a16140305113d1b083e03481f"
chiave_ascii = "gabibbo"

testo_bytes = bytes.fromhex(testo_hex)
chiave_bytes = chiave_ascii.encode()

risultato_bytes = bytes([testo_bytes[i] ^ chiave_bytes[i % len(chiave_bytes)] for i in range(len(testo_bytes))])

risultato_ascii = risultato_bytes.decode(errors="replace")
risultato_hex = risultato_bytes.hex()

print(risultato_ascii)
````

## Code Analysis

1. **Ciphertext**

   The encrypted message is stored in `testo_hex`, which is a long hex string.

2. **Key**

   The ASCII key `"gabibbo"` is used for decryption.

3. **Conversion**
   * `bytes.fromhex(testo_hex)` converts the hex string into raw bytes.
   * The key is encoded into bytes using `.encode()`.

4. **XOR Decryption**

   Each byte of the ciphertext is XORed with the corresponding byte of the key (repeated cyclically).

   ```python
   testo_bytes[i] ^ chiave_bytes[i % len(chiave_bytes)]
   ```

5. **Result**

   * `risultato_ascii` attempts to decode the XORed result as text.
   * `risultato_hex` stores the raw decrypted bytes in hex.
   * Finally, the script prints the ASCII result.

## Exploitation Steps

1. Take the given hex string.
2. Convert it into bytes.
3. Repeat the key `"gabibbo"` over the ciphertext length.
4. XOR each ciphertext byte with the corresponding key byte.
5. Decode the output to reveal the hidden plaintext.

## Solution

Running the script prints the decrypted message, which contains the flag.

```
ITASEC{a_xor_b_equals_to_c_means_c_xor_b_equals_to_a!}
```

## Key Takeaway

This challenge demonstrates a classic **XOR cipher** with a repeating key. Once the key is known, decryption becomes straightforward by reversing the XOR operation.

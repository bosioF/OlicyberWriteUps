import re

with open("100.txt", "r") as f:
    encoded_string = f.read()

decoded_string = encoded_string.replace('0x', '')
decoded_string = re.sub(r'[^0-9a-fA-F]', '', decoded_string)

try:
    #flag = bytes.fromhex(decoded_string).decode('utf-8')
    print(decoded_string)
    #print(flag)
except ValueError as e:
    print(f"Error decoding hex string: {e}")

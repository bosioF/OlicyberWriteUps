dict = 'AAAABAAAAAAAABAABBBAABBABABAAABAABABAABAABBBABAABBAAAAABAABABAABBBBAAA'

def binary_to_string(bits):
    return ''.join([chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)])

nearly_binary_dict = dict.replace('A', '0').replace('B', '1')

flag = binary_to_string(nearly_binary_dict)

print(nearly_binary_dict, f"\n{flag}")

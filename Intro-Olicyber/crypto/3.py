import base64

base64_flag = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE='
bytes_flag = 664813035583918006462745898431981286737635929725

flag1 = base64.b64decode(base64_flag).decode('utf-8')
#print(flag1)
bytes_num = (bytes_flag.bit_length() + 7) // 8
flag2 = bytes_flag.to_bytes(bytes_num,'big').decode('utf-8')

flag = flag1+flag2
print(flag)


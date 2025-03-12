import re

def estrai_flag(path):
    with open(path, 'rb') as file:
        bytes_data = file.read()
        print(bytes_data)
        matches = re.findall(rb'flag\{.*?\}', bytes_data)
        print(matches)


estrai_flag('level1.png')
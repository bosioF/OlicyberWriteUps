import requests
import re

URL = 'http://infinite.challs.olicyber.it/'
FLAG = False

req = requests.session()

def sel_op(page):
    while not FLAG:
        eq = str(re.findall(r'<p>(.*?)</p>', page))
        line = eq.split(' ')
        if "Quante" in eq:
            page = grammar(line)
            if check_flag(page):
                print(FLAG)
                break
        elif "colore" in eq:
            page = art(line)
            if check_flag(page):
                print(FLAG)
                break
        elif "fa" in eq:
            page = math(line)
            if check_flag(page):
                print(FLAG)
                break

def check_flag(page):
    global FLAG
    if "flag" in page:
        FLAG = re.findall(r"<p>(.*?)</p>", page)
        if FLAG:
            return True

def grammar(line):
    letter = line[1].replace('"', '')
    word = line[6].translate(str.maketrans('', '', '"?\']'))
    c = word.count(letter)
    r = req.post(URL, data={"sum": f"{c}"})
    if r.status_code != 200:
        print("fallito grammar()")
    elif r.status_code == 200:
        page = r.text
        print("200")
        return page
    
def art(line):
    color = line[5].replace('?', ' ').replace('\'', ' ').replace(']', ' ')
    r = req.post(URL, data={'color':f"{color}"})
    if r.status_code != 200:
        print("fallito art()")
    elif r.status_code == 200:
        page = r.text
        print("200")
        return page

def math(line):
    num1 = line[2]
    num2 = line[4].replace('?', ' ').replace('\'', ' ').replace(']', ' ')
    sum = int(num1) + int(num2)
    r = req.post(URL, data={"sum":f"{sum}"})
    if r.status_code != 200:
        print("fallito math()")
    elif r.status_code == 200:
        page = r.text
        print("200")
        return page

if __name__ == "__main__":
    r = req.get(URL).text
    sel_op(page=r)
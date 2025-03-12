import os
import base64
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json
from flask import Flask, request, render_template, redirect, url_for, request, make_response
from secret import FLAG


cookie_key = os.getenv('SESSION_SECRET', 'segreto_segreto').encode()

app = Flask(__name__)


def decrypt_session(session):
    try:
        session = base64.b64decode(session)
        iv = session[:16]
        cipher = session[16:]

        aes = AES.new(cookie_key, AES.MODE_CBC, iv)

        decrypted = aes.decrypt(cipher)
        decrypted = unpad(decrypted, 16)
        return decrypted.decode('utf-8')
    except:
        return None


def make_new_state():
    return {
        'next': random.randint(1, 3),
        'visited': []
    }


def get_state():
    session = request.cookies.get('session')
    if session is None:
        return make_new_state()

    state = decrypt_session(session)
    if state is None:
        return make_new_state()

    try:
        return json.loads(state)
    except:
        return make_new_state()


def set_state(state):
    iv = os.urandom(16)
    aes = AES.new(cookie_key, AES.MODE_CBC, iv)
    state = json.dumps(state).encode('utf-8')
    state = pad(state, 16)
    cipher = aes.encrypt(state)
    session = iv + cipher
    session = base64.b64encode(session).decode('utf-8')

    return session


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        state = get_state()
        print(state)

        if len(state['visited']) == 10:
            return render_template("flag.html", flag=FLAG)

        response = make_response(render_template("index.html"))
        response.set_cookie('session', set_state(state))
        return response
    
    if request.method == "POST":
        state = get_state()
        print(state)
        choice = request.form.get('choice')

        if choice is None:
            return redirect(url_for('index'))

        try:
            choice = int(choice)
        except:
            return redirect(url_for('index'))

        if len(state['visited']) == 10:
            response =  make_response(render_template("flag.html", flag=FLAG))
            response.set_cookie('session', set_state(state))
            return response

        if state['next'] == choice:
            state['visited'].append({
                'choice': choice
            })
            state['next'] = random.randint(1, 3)
        else:
            state = make_new_state()

        response = make_response(redirect(url_for('index')))
        response.set_cookie('session', set_state(state))
        return response


if __name__ == "__main__":
    app.run(debug=True)
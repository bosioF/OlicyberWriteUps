from flask import Flask, request, render_template, send_from_directory
import os
from config import DEVICE_MEMORY

app = Flask(__name__)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-picture')
def getPicture():
    id = int(request.args['id'])

    if id > 4:
        return '???'

    return DEVICE_MEMORY[id]


if __name__ == '__main__':
    app.run(debug=True)

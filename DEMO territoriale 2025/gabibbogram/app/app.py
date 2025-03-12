import io
import time
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
import os

FLAG = 'flag{redacted}'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 # 16 KB

@app.route('/', methods=['GET'])
def index():
	return redirect(url_for('gallery'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(url_for('upload'))
		
		file = request.files['file']
		filename = f"{int(time.time()):08x}{os.urandom(4).hex()}.jpg"
		file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
		file.save(file_path)

		return redirect(url_for('upload'))
	return render_template('upload.html')

@app.route('/gallery', methods=['GET'])
def gallery():
	files = sorted(os.listdir(app.config['UPLOAD_FOLDER']))
	return render_template('gallery.html', images=files)

@app.route('/image', methods=['GET'])
def image():
	filename = request.args.get('filename')
	file_path = f"{app.config['UPLOAD_FOLDER']}/{filename}"
	with open(file_path, 'rb') as f:
		file_bytes = io.BytesIO(f.read())
	return send_file(file_bytes, mimetype='image/jpeg')

# if __name__ == '__main__':
# 	app.run(debug=True)
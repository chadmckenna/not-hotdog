import os
from flask import Flask, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from model import predict

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return 'Hello, Hotdog!'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/is_hotdog', methods=['POST'])
def is_hotdog():
    print(request.files)
    if 'file' not in request.files:
        return redirect('/')

    file = request.files['file']

    if file.filename == '':
        return redirect('/')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        predictions = predict(file_path)
        return jsonify({'what': predictions[0], 'probability': predictions[1].tolist()})

    return 'Nope'

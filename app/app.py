import os
from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from model import predict as predict_simple
from model_connected import predict as predict_connected

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

@app.route('/')
def index():
    return 'Hello, Hotdog!'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/is_hotdog', methods=['OPTIONS', 'POST'])
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
        merged = merge_predictions(predict_simple(file_path), predict_connected(file_path))
        return jsonify(
                {'what': merged[0], 'probability': merged[1]},
            )

    return 'Nope'


def merge_predictions(model1, model2):
    mean = (model1[1] + model2[1]) / 2

    if mean > 0.8:
        return 'hotdog', mean
    else:
        return 'not hotdog', mean

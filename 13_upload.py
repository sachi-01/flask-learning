import webbrowser
from flask import Flask, render_template, redirect, request, url_for, abort, flash
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = 'any readom string'


@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST', 'GET'])
def uoload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
    return 'file upload successfully'


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()

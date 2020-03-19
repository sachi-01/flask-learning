import webbrowser
from flask import Flask, render_template, redirect, request, url_for, abort

app = Flask(__name__)
app.secret_key = 'any readom string'


@app.route('/')
def index():
    return render_template('log_in.html')


@app.route('/login', methods=['POST','GET'])
def login():
    # if request.method == 'POST' and request.form['username'] == 'admin':
    #     return redirect(url_for('success'))
    # return redirect(url_for('index'))
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in seccessfully'



if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()


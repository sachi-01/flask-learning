import webbrowser
from flask import Flask, render_template, redirect, request, url_for, abort, flash

app = Flask(__name__)
app.secret_key = 'any readom string'


@app.route('/')
def index():
    return render_template('12_log_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('12_login.html', error=error)


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()

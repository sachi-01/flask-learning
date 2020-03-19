import webbrowser
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('9_index.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('9_readcookie.html'))
    resp.set_cookie('userID', user)

    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    # name = 'admin'
    return '<h1>welcome '+name+' </h1>'


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()
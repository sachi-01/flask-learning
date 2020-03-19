import webbrowser
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/7_index.html")

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()
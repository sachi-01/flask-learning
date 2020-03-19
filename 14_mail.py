import webbrowser
from flask import Flask, render_template, redirect, request, url_for, abort, flash
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Hello', sender='yourId@gmail.com', recipients=['id1@gmail.com'])
    msg.body = 'This is the email body'
    mail.send(msg)
    return 'Sent'


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()


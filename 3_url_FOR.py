from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_Flask():
    return 'Hello_Flask'

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'


@app.route('/guest')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest', guest = name))#url_for()的返回值位query_user对应的url地址

if __name__ == '__main__':
     app.run()
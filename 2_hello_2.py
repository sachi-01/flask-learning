from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'hello_flask'

@app.route('/python/')
def hello_python():
   return 'hello_python'


if __name__ == '__main__':
   app.run()
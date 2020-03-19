import webbrowser
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('8_student.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('8_result.html', result=result)

if __name__ =='__main__':
    webbrowser.open('http://127.0.0.1:5000')
    app.run()

from  flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('hello.html')
#
# @app.route('/hello/<user>')
# def hello_name(user):
#     return render_template('hello.html',name=user)
#
# @app.route('/hello/<int:score>')
# def hello_name(score):
#     return render_template('hello.html', marks=score)

@app.route('/result')
def result():
    dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('5_result.html', result=dict)


if __name__ == '__main__':
    app.run()
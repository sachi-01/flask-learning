from flask import Flask,redirect,url_for,request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method =="POST":
        user = request.form['nm']#由于服务器通过POST方法接收数据，因此通过以下步骤获得从表单数据获得的“nm”参数的值：
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')#服务器上接收的数据是通过GET方法获得的。通过以下的步骤获得'nm'参数的值：
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
    app.run()


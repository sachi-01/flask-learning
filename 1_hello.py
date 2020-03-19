from flask import Flask
app = Flask(__name__)

# app.route(rule, options)
# rule 参数表示与该函数的URL绑定。
# options 是要转发给基础Rule对象的参数列表。
# 一
# @app.route('/')
# def hello_world():
#    return 'hello_world'

#二
# @app.route('/hello')
# def hello_1():
#    return 'this is test the app.route(\'/hello\')'

# 三 等同于一
@app.route('/hello')
def hello_2():
   return 'this is test the app.add_url_rule(\'/\', \'hello\', hello_world)'
app.add_url_rule('/', 'hello', hello_2) #设置路由规则 设置默认路径

@app.route('/blog/<int:name>')
def hello_blog(name):
   return 'hello %d' % name

@app.route('/rev/<float:name>')
def hello_rev(name):
   return 'hello %f' % name

if __name__ == '__main__':
   app.run()
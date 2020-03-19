from flask import Flask,request,url_for
app=Flask(__name__)


@app.route('/')
def Index():
    return  "<h1>this is Index Page</h1>"

@app.route('/ssss')
def query_user():
    """
      http://127.0.0.1:5000/test?id=123
    :return:
    """
    id = request.args.get('id')
    return "query user:"+id

@app.route('/query_url')
def query_url():
    """
    反导向query_user函数名对应的url地址
    :return
    """
    return  "query url: "+url_for("query_user")

if __name__ == "__main__":
    app.run(debug=True)
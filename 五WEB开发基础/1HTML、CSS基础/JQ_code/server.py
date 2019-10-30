import json


from flask import Flask
from flask import request
from flask import Response


app = Flask(__name__)

@app.route("/")
def index():
    resp = Response("<h2>首页</h2>")
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route("/course")
def courses():
    resp = Response(json.dumps({
        'name':'张三'
    }))
    resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp

@app.route("/create",methods=["post",])
def  create():
    print(request.form.get('name'))

    with open(file='user.json',mode='r',encoding='utf8') as f:
        #将数据反序列化
        data = json.loads(f.read())

    data.append({'name':request.form.get('name')})

    with open(file="user.json",mode='w',encoding="utf8") as  f:
        f.write(json.dumps(data))

    resp = Response(json.dumps(data))

    resp.headers["Access-Control-Allow-Origin"] = "*"

    return resp

if __name__ == '__main__':
    app.run(host="localhost",port=8800)

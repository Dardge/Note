from flask import Flask, render_template, request
import json

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/ajaxDB"

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(30))
    upwd = db.Column(db.String(30))
    uemail = db.Column(db.String(120))

    # 声明一个函数-to_dict
    # 为了将本类中所有的属性都封装到一个字典中并返回
    def to_dict(self):
        dic = {
            'id': self.id,
            'uname': self.uname,
            'upwd': self.upwd,
            'uemail': self.uemail
        }
        return dic


class Province(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(30))
    cities = db.relationship(
        "City",
        backref="province",
        lazy="dynamic"
    )

    def to_dict(self):
        dic = {
            "id":self.id,
            "pname":self.pname
        }
        return dic


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30))
    pid = db.Column(db.Integer, db.ForeignKey('province.id'))

    def to_dict(self):
        dic = {
            "id":self.id,
            "cname":self.cname,
            "pid":self.pid
        }
        return dic

db.create_all()

@app.route('/01-json')
def json01():
    return render_template("01-json.html")


@app.route('/02-json-server')
def json_server():
    # 1.声明一个字典,并转换为JSON串
    # dic = {
    #     'uname':'MrQi',
    #     'uage':30,
    #     'ugender':'Male',
    # }
    # 2.通过json.dumps将dic转换为字符串
    # jsonStr = json.dumps(dic)
    # print(jsonStr)
    # return jsonStr


    # 使用列表来表示多个对象
    # 对象1: uname:MrQi,uage:26
    # 对象2: uname:MrLv,uage:30
    # 对象3: uname:MrWei,uage:40
    # 将列表转换成JSON格式的字符串再响应
    uList = [
        {
            "uname": "MrQi",
            'uage': 26
        },
        {
            "uname": "MrLv",
            'uage': 30
        },
        {
            "uname": "MrWei",
            'uage': 40
        },
    ]

    jsonStr = json.dumps(uList)
    return jsonStr


@app.route('/03-json-db')
def json_db():
    users = User.query.all()
    # 循环遍历users中的每个对象,将每个对象调用其to_dict()转换成字典,再追加到一个新列表中
    uList = []
    for u in users:
        uList.append(u.to_dict())
    # 将uList转换为JSON格式的字符串
    jsonStr = json.dumps(uList)
    return jsonStr


@app.route('/04-users')
def users_views():
    return render_template("04-users.html")


@app.route('/04-server')
def server04():
    # 1.查询所有的user的信息
    users = User.query.all()
    # 2.将user的信息转换成字典再保存进列表
    list = []
    for u in users:
        list.append(u.to_dict())
    # 3.将列表响应
    return json.dumps(list)


@app.route('/05-load')
def load_views():
    return render_template("05-load.html")


@app.route("/06-jq-get")
def jq_get():
    return render_template("06-jq-get.html")


@app.route("/06-server")
def server06():
    # 方式1的响应处理
    # return "这是使用$.get()发送的get请求"

    # 方式2的响应处理
    # uname = request.args['uname']
    # uage = request.args['uage']
    # return "用户名称:%s,用户年龄:%s" % (uname,uage)

    # 方式3:响应回去的数据是JSON的串
    list = [
        {
            'uname': '潘金莲',
            'uage': 22
        },
        {
            'uname': '嫦娥',
            'uage': 25
        },
        {
            'uname': '刘姥姥',
            'uage': 88
        }
    ]
    return json.dumps(list)


@app.route("/07-jq-ajax")
def jq_ajax():
    return render_template("07-jq-ajax.html")


@app.route("/07-server")
def server07():
    list = [
        {
            'uname': '潘金莲',
            'uage': 22
        },
        {
            'uname': '嫦娥',
            'uage': 25
        },
        {
            'uname': '刘姥姥',
            'uage': 88
        }
    ]
    return json.dumps(list)


@app.route("/08-register")
def register():
    return render_template("08-register1.html")


@app.route("/08-checkuname")
def checkuname():
    uname = request.args['uname']
    user = User.query.filter_by(uname=uname).first()
    if user:
        dic = {
            "status": 1,
            "text": "uname already exist"
        }
    else:
        dic = {
            "status": 0,
            "text": "uname does not exist"
        }
    return json.dumps(dic)


@app.route('/08-reguser', methods=['POST'])
def reguser():
    uname = request.form['uname']
    upwd = request.form['upwd']
    uemail = request.form['uemail']
    user = User()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail
    try:
        db.session.add(user)
        db.session.commit()
        dic = {
            "status": 1,
            "text": "register success"
        }
        return json.dumps(dic)
    except Exception as ex:
        print(ex)
        dic = {
            "status": 0,
            "text": "register failed"
        }
        return json.dumps(dic)

@app.route('/09-address')
def address_views():
    return render_template('09-address.html')

@app.route('/10-province')
def get_province():
    provinces = Province.query.all()
    list = []
    for pro in provinces:
        list.append(pro.to_dict())
    return json.dumps(list)

@app.route('/10-city')
def get_city():
    # 接收前端传递过来的pid的值,表示要查询的城市们所对应的省份id
    pid = request.args['pid']
    cities = City.query.filter_by(pid=pid).all()
    list = []
    for c in cities:
        list.append(c.to_dict())
    return json.dumps(list)

@app.route('/11-crossdomain')
def crossdomain():
    return render_template("11-crossdomain.html")

@app.route('/11-server')
def server11():
    return "成功访问到11-server"

@app.route('/12-cross')
def cross():
    return render_template("12-cross.html")

@app.route('/12-server')
def server12():

    #接收前端传递过来的callback参数值,表示的是前端处理业务的方法名称
    cb = request.args['callback']
    #查询User中的所有的数据并交给前端进行显示
    users = User.query.all()
    list = []
    for u in users:
        list.append(u.to_dict())
    jsonStr = json.dumps(list)
    return cb + "("+jsonStr+");"

if __name__ == "__main__":
    app.run(debug=True)

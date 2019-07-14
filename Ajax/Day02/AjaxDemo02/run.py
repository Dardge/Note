from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/ajaxDB"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    uname = db.Column(db.String(30))
    upwd = db.Column(db.String(30))
    uemail = db.Column(db.String(120))

db.create_all()

@app.route('/01-ajax-get')
def ajax_get():
    return render_template("01-ajax-get.html")

@app.route('/01-server')
def server01():
    return "这是使用ajax发送的get请求"

@app.route('/02-ajax-get')
def ajax_get02():
    return render_template("02-ajax-get.html")

@app.route('/02-server')
def server02():
    uname = request.args['uname']
    return "欢迎:"+uname

@app.route('/03-register')
def register():
    return render_template('03-register1.html')

@app.route('/03-checkuname')
def checkuname():
    uname = request.args['uname']
    user = User.query.filter_by(uname=uname).first()
    if user:
        #返回1表示用户名称已存在
        return "1"
    else:
        #返回0表示通过
        return "0"

@app.route('/03-reg',methods=['POST'])
def reg():
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
        return "注册成功"
    except Exception as ex:
        print(ex)
        return "注册失败"

@app.route('/04-post')
def post():
    return render_template("04-post.html")

@app.route('/04-server',methods=['POST'])
def server04():
    uname = request.form['uname']
    return "欢迎:"+uname

@app.route('/05-users')
def users_views():
    users = User.query.all()
    s = ""
    for u in users:
        s += "%s_%s_%s_%s|" % (u.id,u.uname,u.upwd,u.uemail)
    s = s[0:-1]
    print(s)
    return s

@app.route('/05-showusers')
def showusers():
    return render_template("05-showusers.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, make_response, request, render_template,session

app = Flask(__name__)
app.config['SECRET_KEY'] = "xieshadouxing"

@app.route('/01-setcookie')
def setcookie():
    #保存用户名和密码进cookies
    #通过make_reponse,将响应的字符串封装起来
    resp = make_response("保存cookies成功")
    resp.set_cookie("uname","qtx",60*60*24*365)
    resp.set_cookie("upwd","lzmaria")
    return resp

@app.route('/02-getcookie')
def getcookie():
    if 'uname' in request.cookies:
        uname = request.cookies['uname']
        print("uname的值为:"+uname)
    upwd = request.cookies.get('upwd','密码为空')
    print("upwd的值为:"+upwd)
    return "获取cookies的值成功!"

@app.route('/03-delcookie')
def delcookie():
    resp = make_response("删除cookie成功")
    if 'uname' in request.cookies:
        resp.delete_cookie('uname')
    return resp

@app.route('/04-login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        #判断cookeis中是否有 uname
        if 'uname' in request.cookies:
            #判断uname的值是否为admin
            uname = request.cookies['uname']
            if uname == 'admin':
                return "欢迎%s回来,<a href='/05-logout'>退出</a>" % uname
        return render_template("04-login.html")
    else:
        #接收用户名和密码并判断是否正确
        uname = request.form['uname']
        upwd = request.form['upwd']
        if uname == 'admin' and upwd == 'admin':
            #登录成功
            resp = make_response("欢迎%s登录,<a href='/05-logout'>退出</a>" % uname)

            #判断是否要记住密码
            if 'isSaved' in request.form:
                resp.set_cookie('uname',uname,60*60*24*31*3)

            return resp
        else:
            return "<script>alert('登录失败');location.href='/04-login';</script>"



@app.route('/05-logout')
def logout():
    if 'uname' in request.cookies:
        resp = make_response("退出成功")
        resp.delete_cookie('uname')
        return resp
    return "退出成功"

@app.route('/06-setsession')
def setsession():
    session['uname'] = 'lvzemaria'
    return "保存数据进session成功!"

@app.route('/07-getsession')
def getsession():
    if 'uname' in session:
        uname = session['uname']
        print("uname:"+uname)
    else:
        print("session中没有uname的值")

    return "获取数据成功!"

if __name__ == "__main__":
    app.run(debug=True)
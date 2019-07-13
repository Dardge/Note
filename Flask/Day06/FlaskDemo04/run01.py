from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import or_, func
import math

# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 连接到MySQL中flaskDB数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskDB"
# 指定不需要信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 指定程序的启动模式为调试模式
app.config['DEBUG'] = True
# 指定执行完增删改之后的自动提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 创建SQLAlchemy的实例
db = SQLAlchemy(app)

# 创建Manager对象并指定要管理的app
manager = Manager(app)
# 创建Migrate对象,并指定关联的app和db
migrate = Migrate(app, db)
# 为manager增加数据库的迁移指令
# 为manager增加一个子命令-db(自定义),具体操作由MigrateCommand来提供
manager.add_command('db', MigrateCommand)


# 创建实体类-Users,映射到数据库中叫users表
# 创建字段id,主键,自增
# 创建字段username,长度为80的字符串,不能为空,值唯一,加索引
# 创建字段age,整数,允许为空
# 创建字段email,长度为120的字符串,必须唯一
class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(80),
        nullable=False,
        unique=True,
        index=True
    )

    age = db.Column(
        db.Integer,
        nullable=True
    )

    email = db.Column(
        db.String(120),
        unique=True
    )

    # 增加一个列isActive,默认为True
    isActive = db.Column(db.Boolean, default=True)
    # 增加一个列birthday
    birthday = db.Column(db.Date)

    def __repr__(self):
        return "<User %r>" % self.username


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    # 增加一个外键列-course_id,引用自Course类(course表)的主键id
    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.id')
    )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    # 增加对Teacher的关联属性和反向引用关系属性
    teachers = db.relationship(
        'Teacher',
        backref="course",
        lazy="dynamic"
    )


class Wife(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30))


# 先删除所有表结构
# db.drop_all()

# 将所有的实体类生成对应的表结构
# 前提:表不存在的情况下才能生成
# db.create_all()


@app.route('/01-add')
def add_views():
    # 1.创建Users的对象并赋值
    user = Users()
    user.username = "祁QTX"
    user.age = 30
    user.email = "tianxuan.qi@163.com"
    user.birthday = "2005-10-12"
    # 2.将Users的对象保存回数据库
    db.session.add(user)
    # 3.提交事务
    # db.session.commit()
    # 4.响应一句话
    return "增加数据成功"


@app.route('/02-reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'GET':
        return render_template('02-reg.html')
    else:
        # 1.接收前端传递过来的数据并创建Users对象
        user = Users()
        user.username = request.form['username']
        user.age = request.form['age']
        user.email = request.form['email']
        user.birthday = request.form['birthday']
        if 'isActive' not in request.form:
            user.isActive = False
        # 2.保存
        db.session.add(user)
        return "注册成功!!!"


@app.route('/03-query')
def query_views():
    # 1.查询Users实体中的id,username两个列的值
    # query = db.session.query(Users.id,Users.username)
    # print(query)
    # print("type:" , type(query))

    # 2.查询Users实体中所有的数据
    users = db.session.query(Users).all()
    for u in users:
        print("id:%d,用户名:%s,年龄:%d,邮箱:%s" % (u.id, u.username, u.age, u.email))

    # 3.查询Users实体中的第一条数据
    user = db.session.query(Users).first()
    print(user)
    # 4.查询Users实体中共有多少条数据
    count = db.session.query(Users).count()
    print("共有%d条数据" % count)
    return "查询数据成功!"


@app.route('/04-filter')
def filter_views():
    # 1.查询年龄大于25的users的信息
    result = db.session.query(Users).filter(Users.age > 25).all()
    print(result)
    # 2.查询id为2的Users的信息
    result = db.session.query(Users).filter(Users.id == 2).first()
    print(result)
    # 3.查询isActive为True并且年龄大于30岁的Users
    # 方案1:使用多filter()函数
    users = db.session.query(Users).filter(Users.isActive == True).filter(Users.age > 30).all()
    # 方案2:使用filter(条件1,条件2)
    users = db.session.query(Users).filter(Users.isActive == True, Users.age >= 30).all()
    print(users)
    # 4.查询isActive为True或者年龄大于30岁的Users
    # or : 使用　or_ 函数
    # from sqlalchemy import or_
    users = db.session.query(Users).filter(
        or_(
            Users.isActive == True,
            Users.age >= 30
        )
    ).all()
    print(users)

    # 5.查询email中包含an的Users的信息
    # sql:select * from users where email like '%an%'
    # 模糊查询like,需要使用实体类属性提供的like()完成查询
    kw = 'an'  # 模拟查询关键词
    users = db.session.query(Users).filter(
        # Users.email.like('%%%s%%' % kw)
        Users.email.like('%' + kw + '%')
    ).all()
    print(users)

    # 6.查询年龄是30岁,或17岁或45岁的Users的信息
    # 模糊查询in 需要使用实体类属性提供in_函数完成
    users = db.session.query(Users).filter(
        Users.age.in_([30, 17, 45])
    ).all()
    print(users)

    # 7.查询年龄在30-45之间的Users的信息
    # 模糊查询between..and..需要使用实体类属性提供的between(值1,值2)完成查询
    users = db.session.query(Users).filter(
        Users.age.between(30, 45)
    ).all()
    print(users)
    return "执行查询过滤器函数成功!"


@app.route('/05-users')
def user_views():
    # 查询Users中isActive为True的用户的信息
    # users = db.session.query(Users).filter(Users.isActive==True)

    users = db.session.query(Users).filter(
        Users.isActive == True
    )

    # 判断是否有kw参数传递到视图中
    if 'kw' in request.args:
        kw = request.args['kw']
        users = users.filter(
            or_(
                Users.username.like('%' + kw + '%'),
                Users.email.like('%' + kw + '%')
            )
        )
    print(users)
    users = users.all()

    return render_template("05-users.html", params=locals())


@app.route('/06-limit')
def limit_views():
    users = db.session.query(Users).limit(2).offset(2).all()
    print(users)
    return "查询数据成功"


@app.route('/07-page')
def page_views():
    # 变量-pageSize,表示每页显示的记录数量
    pageSize = 2
    # 变量-currentPage,表示当前想看的页数
    currentPage = int(request.args.get('currentPage', 1))
    # 查询第currentPage页的数据
    # 跳过(currentPage-1)*pageSize条数据,再获取前pageSize条数据
    ost = (currentPage - 1) * pageSize
    users = db.session.query(Users).offset(ost).limit(pageSize).all()

    # 通过pageSize和总记录数计算尾页页码
    totalCount = db.session.query(Users).count()
    lastPage = math.ceil(totalCount / pageSize)

    # 计算上一页页码
    # 如果currentPage大于1的话那么上一页就是currentPage-1,否则上一页就是1
    prevPage = 1
    if currentPage > 1:
        prevPage = currentPage - 1

    # 计算下一页页码
    # 如果currentPage小于lastPage的话那么下一页就是currentPage+1,否则下一页就是尾页
    nextPage = lastPage
    if currentPage < lastPage:
        nextPage = currentPage + 1

    return render_template('07-page.html', params=locals())


@app.route('/08-aggr')
def aggregat_views():
    # 查询Users实体中所有人的平均年龄
    # result = db.session.query(func.avg(Users.age)).all()
    # print("平均年龄:%.2f" % result[0][0])
    # 查询Users实体中所有人的平均年龄,总年龄,最大年龄和最小年龄,总人数
    result = db.session.query(
        func.avg(Users.age),
        func.sum(Users.age),
        func.max(Users.age),
        func.min(Users.age),
        func.count(Users.id)
    ).all()
    print(result)
    return "聚合函数查询成功"


@app.route('/09-aggr-exer')
def aggr_exer():
    # 1.查询Users实体中年龄大于18岁的人的平均年龄
    result = db.session.query(func.avg(Users.age)).filter(Users.age > 18).all()
    print(result)
    # 2.查询Users实体中按isActive分组后, 每组的人数是多少
    result = db.session.query(
        Users.isActive,
        func.count(Users.id)
    ).group_by('isActive').all()
    print(result)
    # 3.查询Users实体中按isActive分组后, 组内人数大于2人的组名和人数
    result = db.session.query(
        Users.isActive,
        func.count(Users.id)
    ).group_by('isActive').having(
        func.count(Users.id) > 2
    ).all()
    print(result)
    # 4.查询users表中年龄大于18岁的，按照isActive分组，组内人数大于2人的组名和人数查询出来
    result = db.session.query(
        Users.isActive,
        func.count(Users.id)
    ).filter(
        Users.age > 18
    ).group_by(
        'isActive'
    ).having(
        func.count(Users.id) > 2
    ).all()
    print(result)

    # 查询users表中年龄大于"赵金多"的users们的信息
    result = db.session.query(Users).filter(
        Users.age > db.session.query(Users.age).filter(Users.username == '赵金多')
    ).all()
    print(result)
    return "查询成功"


@app.route('/10-update')
def update_views():
    # 1.修改　老王　的isActive属性为True
    # user = db.session.query(Users).filter_by(username='老王').first()
    # user.isActive = True
    # db.session.add(user)
    # 2.删除　"赵金多"
    user = db.session.query(Users).filter_by(id=4).first()
    db.session.delete(user)
    return "修改数据成功"


@app.route('/11-upuser', methods=['GET', 'POST'])
def upuser():
    if request.method == 'GET':
        # 1.接收id
        id = request.args['id']
        # 2.按id查询对象
        user = db.session.query(Users).filter_by(id=id).first()
        # 3.将对象发送到模板上
        return render_template('11-upuser.html', user=user)
    else:
        # 1.接收请求的参数
        id = request.form['id']
        # 2.查询出对应的对象
        user = db.session.query(Users).filter_by(id=id).first()
        # 3.为对象赋值
        user.username = request.form['username']
        user.age = request.form['age']
        user.email = request.form['email']
        user.birthday = request.form['birthday']
        if 'isActive' in request.form:
            user.isActive = True
        else:
            user.isActive = False
        # 4.保存回数据库
        db.session.add(user)
        return redirect('/05-users')


@app.route('/12-regtea')
def regtea():
    # 1.通过teacher对象的course_id属性插入关联的数据
    # teaQi = Teacher()
    # teaQi.tname = "祁老师"
    # teaQi.tage = 30
    # teaQi.course_id = 1
    # db.session.add(teaQi)
    # 2.通过teacher对象的course属性插入关联数据
    # 2.1查询出"Python高级"对象
    course = Course.query.filter_by(cname='Python高级').first()
    # 2.2声明tea对象,并关联查询出的course对象
    tea = Teacher()
    tea.tname = "吕泽Maria"
    tea.tage = 31
    tea.course = course  # 底层是将course.id给了tea.course_id属性
    db.session.add(tea)
    return "插入关联数据成功!"


if __name__ == "__main__":
    # app.run(debug=True)
    # 启动服务的操作交给manager来管理
    manager.run()

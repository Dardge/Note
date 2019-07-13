from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# import pymysql
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 连接到MySQL中flaskDB数据库
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/flaskDB"
# 指定不需要信号追踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 指定程序的启动模式为调试模式
app.config['DEBUG'] = True
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


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)


class Wife(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30))


# 先删除所有表结构
# db.drop_all()

# 将所有的实体类生成对应的表结构
# 前提:表不存在的情况下才能生成
# db.create_all()


if __name__ == "__main__":
    # app.run(debug=True)
    # 启动服务的操作交给manager来管理
    manager.run()

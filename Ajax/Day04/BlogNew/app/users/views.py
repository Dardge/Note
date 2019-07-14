from . import users


@users.route('/users/login')
def users_login():
    return "这是登录的访问路径"

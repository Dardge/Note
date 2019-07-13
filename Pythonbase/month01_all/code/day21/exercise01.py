"""
    练习1：在现有功能上，增加验证权限。
"""

def verify_permission(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        # if 成功:
        return func(*args, **kwargs)
    return wrapper

@verify_permission
def enter_background():
    print("进入后台系统...")

@verify_permission
def delete_order(order_id):
    print("删除订单",order_id)

enter_background()
delete_order(101)
















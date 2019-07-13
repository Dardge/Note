from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
# 订单页
# @login_required(login_url='/user/login/')
# def order(request, order_id=None):
#     if request.method == 'GET':
#         if order_id:
#             orders = Order.objects.filter(id=order_id)
#         else:
#             orders = Order.object.all()
#         for order in orders:
#             order_info=OrderInfo.objects.filter(order=order).first()
#             goods=order_info.goods
#         # 显示订单详情
#         return render(request, 'order/order.html', locals())

# 修改订单
# 支付

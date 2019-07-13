from django.db import models
from user.models import User
from goods.models import Goods


# Create your models here.
# 订单信息
# class Order(models.Model):
#     # 状态
#     is_Active = models.BooleanField('是否结算', default=False)
#     # 实际价格
#     price = models.DecimalField('实际价格', max_digits=8, decimal_places=2)
#     # 关联买家
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='买家')
#     # 关联卖家
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='商家')
#
#     def __str__(self):
#         return '%s:%s' % (self.id, self.is_Active)
#
#     class Meta:
#         db_table = 'order'
#
#
# # 订单商品信息
# class OrderInfo(models.Model):
#     # 关联订单信息
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='订单')
#     # 关联商品
#     goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品')
#     # 关联商品卖家
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='商家')
#     # 交易时价格
#     transaction_price = models.DecimalField('交易价格', max_digits=8, decimal_places=2)
#
#     def __str__(self):
#         return '%s:%s' % (self.order, self.goods)
#
#     class Meta:
#         db_table = 'OrderInfo'

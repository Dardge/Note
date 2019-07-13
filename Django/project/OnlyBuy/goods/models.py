from django.db import models
from user.models import User


# Create your models here.
class GoodsType(models.Model):
    title = models.CharField('分类名称', max_length=30, null=False, default='分类名称')
    is_delete = models.BooleanField('是否下架', default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'GoodsType'


class Goods(models.Model):
    title = models.CharField('商品名称', max_length=100, default='商品名称')
    desc = models.CharField('商品描述', max_length=1000, null=True)
    # '["images/goods/1.png",]'
    goods_images = models.CharField('商品图列表', max_length=1000, default='[]')
    detail_images = models.CharField('商品详情图列表', max_length=1000, default='[]')
    goods_type = models.ForeignKey(GoodsType, on_delete=models.CASCADE, verbose_name='商品类型')
    spec_name = models.CharField('商品规格', max_length=20, default='规格')

    # 商品需要有自己的卖家 卖家也是用户
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='商品卖家')
    is_seller_empower = models.BooleanField('卖家上架', default=True)
    is_admin_empower = models.BooleanField('管理员审批', default=False)
    is_delete = models.BooleanField('商品无效', default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goods'


class GoodsSpecification(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品')
    price = models.DecimalField('此规格的价格', max_digits=8, decimal_places=2)
    spec_info = models.CharField('规格信息', max_length=100, null=False)
    stock = models.IntegerField('库存', default=1, null=False)

    def __str__(self):
        return '%s,价格：%s' % (self.spec_info, self.price)

    class Meta:
        db_table = 'GoodsSpecification'

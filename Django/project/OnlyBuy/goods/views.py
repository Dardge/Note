from django.shortcuts import render
from .models import *
from django.http import Http404
from django.db import DatabaseError


# Create your views here.
def goods_list(request, type_id=None):
    if type_id:
        # 获取所有的商品，到页面中展示
        # 通过type_id查找商品
        # 列出符合条件的商品(type_id为当前的type_id、未过期、是当前卖家的商品、管理员同意)
        # try:
        #     goods_type = GoodsType.objects.filter(id=type_id)
        #     goods = Goods.objects.filter(goods_type_id=type_id, is_delete=False,
        #                                  is_seller_empower=True, is_admin_empower=True)
        # except:
        #     # 未通过type_id查找
        #     # 列出符合条件的商品(未过期、当前卖家的商品、管理员同意)
        #     goods = Goods.objects.filter(is_delete=False, is_seller_empower=True,
        #                                  is_admin_empower=True)

        goods_type = GoodsType.objects.filter(id=type_id)
        goods = Goods.objects.filter(goods_type_id=type_id, is_delete=False,
                                     is_seller_empower=True, is_admin_empower=True)
        if not (goods_type and goods):
            goods = Goods.objects.filter(is_delete=False, is_seller_empower=True,
                                         is_admin_empower=True)

    else:
        # 如果没有type_id
        goods = Goods.objects.filter(is_delete=False, is_seller_empower=True,
                                     is_admin_empower=True)

    # 展示的商品信息
    # 遍历商品列表
    for a_product in goods:
        # 图片
        s = a_product.goods_images
        goods_images = eval(s)
        # 取列表的第一张图作为商品的主图片显示
        try:
            # 添加临时属性:商品的主图片
            a_product.head_images = '/static/images/goods/' + str(a_product.id) + '/' + goods_images[0]
        except IndexError:
            # 显示默认图片
            a_product.head_images = '/static/images/default.png'
        # 价格
        # 使用商品对象去查找对应的商品规格
        # goods_specs = GoodsSpecification.objects.filter(goods_id=a_product.id)
        goods_specs = GoodsSpecification.objects.filter(goods=a_product)
        # 使用第一个商品规格的价格作为商品的价格
        try:
            a_product.price = goods_specs[0].price  # 添加临时属性：商品价格
        except IndexError:
            a_product.price = 998  # 默认价格
    return render(request, 'goods/product_list.html', locals())


def detail(request, goods_id, spec_id=None):
    if spec_id:
        aspec = GoodsSpecification.objects.filter(id=spec_id).first()
        a_goods = Goods.objects.filter(id=aspec.goods_id).first()
        if not aspec:
            raise Http404()
        goods_id = a_goods.id
    else:
        # 获取商品id
        a_goods = Goods.objects.filter(id=goods_id).first()
    if not a_goods:
        raise Http404()
    # 通过商品id查找商品
    # 处理显示
    title = a_goods.title
    desc = a_goods.desc
    # 图片
    image_list = eval(a_goods.goods_images)
    image_list = ['/static/images/goods/' + str(a_goods.id) + '/' + img for img in image_list]
    # 如果图片列表能获取到 第一个作为主图
    if image_list:
        head_image = image_list[0]
    # 否则显示默认图片
    else:
        head_image = '/static/images/default.png'
    # 页面下方的详情大图片
    detail_list = eval(a_goods.detail_images)
    # 展示商品规格
    goods_specs = GoodsSpecification.objects.filter(goods_id=a_goods.id)
    # 如果没找到 返回404
    if not goods_specs:
        raise Http404()
    # 以下逻辑判断当前为哪个规格
    # 如果没有传递规格参数 默认第一个商品的价格就是尚帕尼的价格
    if not spec_id:
        spec_id = goods_specs[0].id
    else:
        spec_id = int(spec_id)
    for item in goods_specs:
        if spec_id == item.id:
            price = item.price
            # 添加一个临时属性 确认哪个规格对象被选择
            item.is_select = True
    # 通过点击按钮  通过路由传递spec_id到视图中
    return render(request, 'goods/product_details.html', locals())

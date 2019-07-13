from django.db import models
from django.contrib.auth.models import AbstractUser

# 自定义用户类型
# 创建时显示的是后面的字符串，传递值时使用的是前面的数字
USERTYPE = ((0, '管理员'), (1, '买家'), (2, '卖家'))
GENDER = (('1', '男'), ('0', '女'))


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField('昵称', max_length=30, null=True, blank=True)
    phone = models.CharField('手机', max_length=30, null=True, unique=True)
    gender = models.CharField('性别', max_length=10, null=True, blank=True, choices=GENDER, default='1')
    usertype = models.IntegerField('用户类型', choices=USERTYPE, default=2)  # 0 管理员，1，卖家，2买家
    is_delete = models.BooleanField('是否禁用用户', default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'user'

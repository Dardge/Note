from django.db import models


# Create your models here.
class User(models.Model):
    uname = models.CharField('姓名', max_length=20)
    upwd = models.CharField('密码', max_length=50)
    uphone = models.CharField('手机', max_length=11, unique=True)
    uemail = models.CharField('邮箱', max_length=200)
    isActive = models.BooleanField(default=True, verbose_name='状态')

    def __str__(self):
        return '%s' % self.uname

    class Meta:
        db_table = 'users'

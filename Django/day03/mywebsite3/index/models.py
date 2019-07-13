from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField('姓名', max_length=20, unique=True, db_index=True)  # 第一个参数内容默认为verbose_name
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True, verbose_name='邮箱')
    isActive = models.BooleanField('状态', default=True)

    def __str__(self):
        return '%s.%s' % (self.id, self.name)

    class Meta:
        # 指定映射到数据库中的表明
        db_table = 'author'
        # 定义在后台界面的名称（单数）
        verbose_name = 'author'
        # 定义在后台界面的名称（复数）
        verbose_name_plural = 'author'


class Wife(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    # 一对一映射,在需要关联的两个类中任意一个类中增加(这里在wife类中增加和author的一对一关联属性)
    author = models.OneToOneField(Author)

    def __str__(self):
        return '%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='书籍')
    pub_date = models.DateTimeField('发布时间', db_index=True)
    publisher = models.ForeignKey('Publisher', null=True, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return '%s.%s' % (self.id, self.title)

    class Meta:
        db_table = 'book'
        verbose_name = 'book'


class Publisher(models.Model):
    name = models.CharField(max_length=20, unique=True, db_index=True, verbose_name='出版社')
    address = models.CharField('地址', max_length=120)
    city = models.CharField('城市', max_length=50)
    website = models.CharField('网址', max_length=50)

    def __str__(self):
        return '%s.%s' % (self.id, self.name)

    class Meta:
        db_table = 'publisher'

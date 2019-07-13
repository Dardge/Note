from django.db import models


# Create your models here.
class Classname(models.Model):
    name = models.CharField(max_length=20)


class Students(models.Model):
    stu_name = models.CharField(max_length=20, unique=True, db_index=True)
    stu_age = models.IntegerField(default=18)
    stu_sex = models.BooleanField(default=1)
    stu_birthday = models.DateField()
    stu_create_time = models.DateTimeField()
    stu_score = models.FloatField()
    stu_img = models.ImageField(upload_to='static/images')
    stu_email = models.EmailField(unique=True, null=True)
    stu_eyesight = models.DecimalField(max_digits=5, decimal_places=3, null=True)

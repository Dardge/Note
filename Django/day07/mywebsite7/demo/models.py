from django.db import models


# Create your models here.
class MediaPic(models.Model):
    picture = models.ImageField('图片', upload_to='images/')

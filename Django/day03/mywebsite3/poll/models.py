from django.db import models


# Create your models here.
class Questions(models.Model):
    quest = models.CharField(verbose_name='问题', max_length=120, unique=True, db_index=True)

    def __str__(self):
        return '%s.%s' % (self.id, self.quest)

    class Meta:
        db_table = 'questions'


class Answers(models.Model):
    answer = models.CharField('答案', max_length=120)
    total = models.IntegerField('票数', default=0)
    quest = models.ForeignKey('Questions', on_delete=models.CASCADE,
                              verbose_name='问题')  # on_delete=models.CASCADE外键删除后会自动删除

    def __str__(self):
        return '%s.%s' % (self.answer, self.total)

    class Meta:
        db_table = 'answers'

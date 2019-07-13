from django.contrib import admin
from .models import Questions, Answers


# Register your models here.
class QuestionsManager(admin.ModelAdmin):
    list_display = ['id', 'quest']


class AnswersManager(admin.ModelAdmin):
    list_display = ['id', 'quest', 'answer', 'total']


admin.site.register(Questions, QuestionsManager)
admin.site.register(Answers, AnswersManager)

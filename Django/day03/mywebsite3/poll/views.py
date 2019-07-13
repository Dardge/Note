from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def index(request):
    quest_list = Questions.objects.order_by('id')
    return render(request, 'index.html', locals())


def detail(request, id):
    answer_list = Answers.objects.filter(quest_id=id)
    quest = Questions.objects.get(id=id)
    return render(request, 'detail.html', locals())


def vote(request):
    id = request.POST.get('answer')
    answer_obj = Answers.objects.get(id=id)
    answer_obj.total += 1
    answer_obj.save()
    print(answer_obj.id)
    # 跳转到结果页面 需要Questions
    quest = answer_obj.quest
    print(quest.id)
    # http://127.0.0.1:8000/poll/1/result/
    # return redirect('/poll/' + str(quest.id) + '/result')
    return redirect('/poll/' + str(answer_obj.id) + '/result')


# def result(request, id):
#     quest = Questions.objects.get(id=id)
#     answer_list = Answers.objects.filter(quest_id=id).order_by('-total')
#     return render(request, 'result.html', locals())


def result(request, answer_id):
    target_answer = Answers.objects.get(id=answer_id)
    quest_id = target_answer.quest_id
    quest = Questions.objects.get(id=quest_id)
    # answer_list = Answers.objects.filter(quest_id=quest_id).order_by('-total')
    answer_list = quest.answers_set.order_by('-total')  # 通过内置属性实现“一”得“多”
    return render(request, 'result.html', locals())

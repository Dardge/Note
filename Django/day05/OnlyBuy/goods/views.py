from django.shortcuts import render


# Create your views here.
def goods(request):
    return render(request, 'goods/index.html')

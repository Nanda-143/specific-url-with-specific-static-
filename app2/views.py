from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def three(request):
    return render(request,'three.html')


def four(request):
    return HttpResponse('this is four from app2')

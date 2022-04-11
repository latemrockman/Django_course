from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def leo(request):
    return HttpResponse("знак зодиака Лев")

def scorpio(request):
    return HttpResponse("знак зодиака Скорпион")
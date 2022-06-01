from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'feedback/feedback.html', {})


def hello(request):
    return render(request, 'feedback/feedback.html', {})
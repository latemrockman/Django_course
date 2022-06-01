from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):

    if request.method == "POST":
        name = request.POST['name']

        if len(name) == 0:
            return render(request, 'feedback/feedback.html', {'got_error': True})


        return HttpResponseRedirect('/done')

    return render(request, 'feedback/feedback.html', {})


def done(request):

    return render(request, 'feedback/done.html', {})



def hello(request):
    return render(request, 'feedback/feedback.html', {})
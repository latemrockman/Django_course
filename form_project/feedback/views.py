from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.


def index(request):
    if request.method == "POST":                            # если будет POST запрос,
        form = FeedbackForm(request.POST)                   # то мы создаем экземпляр формы при помощи данных из POST запроса

        #name = request.POST['name']
        #surname = request.POST['surname']
        #feedback = request.POST['feedback']

        if form.is_valid():
            form.save()


            return HttpResponseRedirect('/done')

    else:                                                   # если нет POST запроса
        form = FeedbackForm()                               # то мы создаем экзепляр пустой формы


    return render(request, 'feedback/feedback.html', context={'form': form})



def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)

    if request.method == "POST":                            # если будет POST запрос,
        form = FeedbackForm(request.POST, instance=feed)  # то мы создаем экзепляр пустой формы

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
    else:
        form = FeedbackForm(instance=feed)  # то мы создаем экзепляр пустой формы

    return render(request, 'feedback/feedback.html', context={'form': form})



def done(request):
    return render(request, 'feedback/done.html', {})


def hello(request):
    return render(request, 'feedback/feedback.html', {})
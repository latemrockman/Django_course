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
            all_data = form.cleaned_data                    # возвращает словарь с данными из формы (работает только после form.is_valid())

            feed = Feedback(
                name=all_data['name'],
                surname=all_data['surname'],
                feedback=all_data['feedback'],
                rating=all_data['rating']
            )
            feed.save()


            return HttpResponseRedirect('/done')

    else:                                                   # если нет POST запроса
        form = FeedbackForm()                               # то мы создаем экзепляр пустой формы


    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html', {})


def hello(request):
    return render(request, 'feedback/feedback.html', {})
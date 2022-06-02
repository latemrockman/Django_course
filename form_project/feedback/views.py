from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

# Create your views here.


def index(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)

        name = request.POST['name']                         # получить данные через request.POST
        surname = request.POST['surname']
        feedback = request.POST['feedback']

        if form.is_valid():
            all_data = form.cleaned_data                    # возвращает словарь с данными из формы (работает только после form.is_valid())
            return HttpResponseRedirect('/done')
    form = FeedbackForm()

    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html', {})


def hello(request):
    return render(request, 'feedback/feedback.html', {})
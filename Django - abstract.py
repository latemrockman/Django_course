"""
в командной строке:
django-admin			                # вывести список команд
django-admin startproject first         # создать проект first
"""

############################################################################################################
создание проекта

1. django-admin startproject first      # создать проект first
2. python manage.py runserver           # запуск локального веб сервера

127.0.0.1 - локальный сервера

http://127.0.0.1:8000/          # локальный сервер
http://localhost:8000/          # то же самое

список всех "приложений" в файле settings.py  в списке INSTALLED_APPS

3. python manage.py startapp video      # создать приложение video (аналог модуля)
4. подключить приложение - в файле settings.py  в список INSTALLED_APPS добавить элемент "video"

############################################################################################################
URLs and Views


1. django-admin startproject my_page            # создали проект my_page
2  python manage.py startapp horoscope          # создали приложение horoscope
3. python manage.py startapp horoscope          # запускае сервер

URL - унифицированный указатель ресурса
Views - представление. код, который выполняется для разных URLs (функция или класс)

на каждый url должен быть свое представление

4. в папке my_page в файле urls.py добавить path('horoscope/leo', leo),
'horoscope/leo' - url
leo - функция в папке horoscope/views.py

функции во views обязательно должны принимать аргумент (принято request)

from horoscope.views import leo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/leo', leo),                 
]

5. добавить в файл views.py 
from django.http import HttpResponse

def leo(request):
    return HttpResponse("знак зодиака Лев")



############################################################################################################
создание URLs config


1. в папке horoscope создать файл urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('leo', views.leo),
    path('scorpio', views.scorpio),
]

2. в файле my_page/urls.py изменить urlpatterns:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include("horoscope.urls")),
]


############################################################################################################
отладка Django in PyCharm

1. нажать кнопку Add Configuration
    -нажать +,
    - выбрать Python,
    - название Zodiak,
    - рабочая дирктория my_page (наш проект)
    - после этого должна подставиться версия Питона
    - Parametrs: manage.py runserver
 








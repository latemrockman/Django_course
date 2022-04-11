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
 


############################################################################################################
Динамический URL

1. в файле views.py создать функцию:

def get_info_about_sign_zodiak(request, sign_zodiak):
    dict_zodiak = {
        "aries"         : "Овен     - 21 марта — 20 апреля",
        "taurus"        : "Телец    - 21 апреля — 20 мая",
        "gemini"        : "Близнецы - 21 мая — 21 июня",
        "cancer"        : "Рак      - 22 июня — 22 июля",
        "leo"           : "Лев      - 23 июля — 23 августа",
        "virgo"         : "Дева     - 24 августа — 23 сентября",
        "libra"         : "Весы     - 24 сентября — 23 октября",
        "scorpio"       : "Скорпион - 24 октября — 22 ноября",
        "sagittarius"   : "Стрелец  - 23 ноября — 21 декабря",
        "capricorn"     : "Козерог  - 22 декабря — 20 января",
        "aquarius"      : "Водолей  - 21 января — 20 февраля",
        "pisces"        : "Рыбы     - 21 февраля — 20 марта",
    }

    if sign_zodiak in dict_zodiak:
        return HttpResponse(dict_zodiak[sign_zodiak])
    else:
        return HttpResponseNotFound(f"{sign_zodiak} - неизвестный знак зодиака")

2. в файле horoscope/urls.py

urlpatterns = [
    path('<sign_zodiak>', views.get_info_about_sign_zodiak),
    #path('leo', views.leo),
    #path('scorpio', views.scorpio),
]

3. в файле my_page/urls.py

удалить - from horoscope.views import leo

############################################################################################################
Конверторы роутов

1. в файле views меняем функцию, словарь переносим в глобальную область

def get_info_about_sign_zodiak(request, sign_zodiak):
    description = dict_zodiak.get(sign_zodiak, None)

    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"{sign_zodiak} - неизвестный знак зодиака")
        
        
##  при запросах несуществующего ключа - статус ответа 404 ()
    при запросах существующего ключа - статус ответа 200
    
    этот статус выставляет сам класс HttpResponse (200) и HttpResponseNotFound (404)


2. в файле urls:

urlpatterns = [
    path('16/', views.get_info_about_16),                                       # если ввели 16
    path('<int:sign_zodiak>/', views.get_info_about_sign_zodiak_by_number),     # если ввели число
    path('<str:sign_zodiak>/', views.get_info_about_sign_zodiak_by_string),     # если ввели строку
]

    преобразование роутов идет сверху вниз (перебор списка), тут сначала пробует преобразовать в число, 
    если это возможно то преобразует, если нет то следующий элемент списка (в строку)
    
3. views:

def get_info_about_sign_zodiak_by_number(request, sign_zodiak: int):
    return HttpResponse(f'это число {sign_zodiak}')


def get_info_about_sign_zodiak_by_string(request, sign_zodiak: str):
    description = dict_zodiak.get(sign_zodiak, None)

    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f"{sign_zodiak} - неизвестный знак зодиака")
        
def get_info_about_16(request):
    return HttpResponse(f'This is 16')
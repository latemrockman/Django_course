from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.



def leo(request):
    return HttpResponse("знак зодиака Лев")

def scorpio(request):
    return HttpResponse("знак зодиака Скорпион")


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

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import datetime


# Create your views here.

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

date_zodiac = {
    "aries": ((3, 21), (4, 20)),
    "taurus": ((4, 21), (5, 20)),
    "gemini": ((5, 21), (6, 21)),
    "cancer": ((6, 22), (7, 22)),
    "leo": ((7, 23), (8, 23)),
    "virgo": ((8, 24), (9, 23)),
    "libra": ((9, 24), (10, 23)),
    "scorpio": ((10, 24), (11, 22)),
    "sagittarius": ((11, 23), (12, 21)),
    "capricorn": ((12, 22), (1, 20)),
    "aquarius": ((1, 21), (2, 20)),
    "pisces": ((2, 21), (3, 20))
}

types = {
    "fire"  : ["aries", "leo", "sagittarius"],
    "earth" : ["taurus", "virgo", "capricorn"],
    "air"   : ["gemini", "libra", "aquarius"],
    "water" : ["cancer", "scorpio", "pisces"]
}

def index(request):
    zodiacs = list(dict_zodiak)

    data = {"menu": zodiacs,
            "dict": dict_zodiak,
            "space": ()}

    return render(request, 'horoscope/index.html', context = data)

def type_index(request):
    types_list = list(types)
    li_types = ""
    for sign in types_list:
        redirect_path = reverse("type-name", args=[sign])
        li_types += f"<li><a href ='{redirect_path}'>{sign.title()}</a> </li>"
    response = f"""
        <ul>
        {li_types}
    </ul>
"""
    return HttpResponse(response)

def get_zodiac_type(request, sign_type: str):
    list_element = types.get(sign_type, None)
    if list_element:
        menu_zodiak = ""
        for znak in list_element:
            redirect_path = reverse("horoscope-name", args=[znak])
            menu_zodiak += f"<li><a href ='{redirect_path}'>{znak.title()}</a></li>"
        response = f"""
        <ul>
            {menu_zodiak}
        </ul>
"""
        return HttpResponse(response)
    else:
        return HttpResponseNotFound(f"{sign_type} - неизвестня стихия")

def get_info_about_sign_zodiak_by_number(request, sign_zodiak: int):
    zodiacs = list(dict_zodiak)
    if sign_zodiak > len(zodiacs):
        return HttpResponseNotFound(f"Был передан неправильный порядковый номер - {sign_zodiak}")
    name_zodiac = zodiacs[sign_zodiak - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)

def get_info_about_sign_zodiak_by_string(request, sign_zodiak: str):
    description = dict_zodiak.get(sign_zodiak)
    #name_title = description.split()[0]
    #zodiacs = list(dict_zodiak)
    data = {
        "description"   : description,
        "sign"          : sign_zodiak,
        "zodiacs"       : dict_zodiak,
#        "name_title"    : name_title
    }

    return render(request, 'horoscope/info_zodiac.html', context=data)

def get_info_about_111(request):
    return HttpResponseRedirect(f'https://mail.ru/')

def get_info_about_555(request):
    return HttpResponse(f'This is 555')

def get_info_by_date(request, month, day):
    response = identify_zodiac_sign(day, month, 0)

    if response == "Некорректная дата":
        return HttpResponseNotFound(f"День: {day}, Месяц: {month}<br>{response}")
    else:
        return HttpResponse(f"День: {day}, Месяц: {month}<br><h2>{dict_zodiak[response]}</h2>")

def identify_zodiac_sign(day, month, year):
    try:
        if year == 0:
            year = datetime.datetime.now().year

        user_date = datetime.date(year, month, day)

        for zodiac, date in date_zodiac.items():
            date_from = datetime.date(year, date[0][0], date[0][1])
            date_to = datetime.date(year, date[1][0], date[1][1])

            if date_from <= user_date and user_date <= date_to:
                return zodiac
        return "capricorn"
    except:
        return "Некорректная дата"

def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали число из четырёх чисел - {sign_zodiac}")

def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f"Вы передали вещественное число - {sign_zodiac}")

def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f"Вы указали дату - {sign_zodiac}")
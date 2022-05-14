from django.contrib import admin
from .models import Movie


# Register your models here.


@admin.register(Movie)                                          # за классом админ указываем клас MovieAdmin
class MovieAdmin(admin.ModelAdmin):                             # класс обычно называют по названию модели + Admin
    list_display = ['name', 'rating', 'year',  'budget']        # перечисляем строками поля из класса Movie, 0й лемент будет ссылкой
    list_editable = ['rating', 'year']                          # перечисляем поля, которые можно редактировать из таблицы, поле 'name' нельзя указывать тк оно будет ссылкой
    ordering = ['rating', '-year']                              # сортировка, по рейтингу первостепенная, по году второстепенная
    list_per_page = 3                                           # сколько записей отображается на 1й странице


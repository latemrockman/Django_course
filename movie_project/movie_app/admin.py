from django.contrib import admin
from .models import Movie


# Register your models here.


@admin.register(Movie)                                                      # за классом админ указываем клас MovieAdmin
class MovieAdmin(admin.ModelAdmin):                                         # класс обычно называют по названию модели + Admin
    list_display = ['name', 'rating', 'year',  'budget', 'rating_status']   # перечисляем строками поля из класса Movie, 0й лемент будет ссылкой
    list_editable = ['rating', 'year']                                      # перечисляем поля, которые можно редактировать из таблицы, поле 'name' нельзя указывать тк оно будет ссылкой
    ordering = ['rating', '-year']                                          # сортировка, по рейтингу первостепенная, по году второстепенная
    list_per_page = 15                                                      # сколько записей отображается на 1й странице

    @admin.display(description='Оценка')                                    # Задать название колонки (по умолчанию название берется по названию метода)
    def rating_status(self, mov: Movie):                                    # rating_status - название колонки, mov - экземпляр класса Movie (название экземпляра может быть любым)
        if mov.rating < 50:
            return "Зачем это смотреть?!"
        if mov.rating < 70:
            return "Разок можно глянуть..."
        if mov.rating <= 85:
            return "Звчет!"
        return "Топчик!"
from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet


# Register your models here.


@admin.register(Movie)                                                                  # за классом админ указываем клас MovieAdmin
class MovieAdmin(admin.ModelAdmin):                                                     # класс обычно называют по названию модели + Admin
    list_display = ['name', 'rating', 'currency', 'year',  'budget', 'rating_status']   # перечисляем строками поля из класса Movie, 0й лемент будет ссылкой
    list_editable = ['rating', 'currency', 'year']                                      # перечисляем поля, которые можно редактировать из таблицы, поле 'name' нельзя указывать тк оно будет ссылкой
    ordering = ['rating', '-year']                                                      # сортировка, по рейтингу первостепенная, по году второстепенная
    list_per_page = 15                                                                  # сколько записей отображается на 1й странице
    actions = ['set_dollars', 'set_euro', 'set_rubles']
    search_fields = ['name__endswith', 'rating']

    @admin.display(description='Оценка')                                                # Задать название колонки (по умолчанию название берется по названию метода)
    def rating_status(self, mov: Movie):                                                # rating_status - название колонки, mov - экземпляр класса Movie (название экземпляра может быть любым)
        if mov.rating < 50:
            return "Зачем это смотреть?!"
        if mov.rating < 70:
            return "Разок можно глянуть..."
        if mov.rating <= 85:
            return "Звчет!"
        return "Топчик!"

    @admin.action(description='Установить валюту в доллар')                             # декоратор указывает, что это действие в админке + название
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)                                                   # update - метод класса Queryset, установить значение currency Movie.USD

        self.message_user(request, 'изменили валюту в рубли', messages.WARNING)         # тип сообщения WARNING

    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_update = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было обновлено {count_update} записей'                                    # сли тип сообщения не указывать, то будет стандартный INFO
        )

    @admin.action(description='Установить валюту в рубли')
    def set_rubles(self, request, qs: QuerySet):
        qs.update(currency=Movie.RUB)

        self.message_user(request, 'изменили валюту в рубли', messages.ERROR)           # тип сообщения ERROR
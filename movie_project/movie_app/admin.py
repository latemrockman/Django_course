from django.contrib import admin, messages
from .models import Movie, Director
from django.db.models import QuerySet



# Register your models here.

admin.site.register(Director)






class RatingFilter(admin.SimpleListFilter):                                             # создаем класс с осмысленным названием, наследуемся обязательно от admin.SimpleListFilter
    title = 'Фильт по рейтингу'                                                         # обязательный атрибут, как будет называться фильтр
    parameter_name = 'rating'                                                           # обязательный атрибут, значение подставляется в url при фильтрации

    def lookups(self, request, model_admin):
        return [                                                                        # возвращаем список из вариантов, которые мы можем выбрать в фильтре, представляет собой списко кортежей
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>= 80', 'Высочайший')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':                                                       # '<40' cравнивает со строкой из списка кортежей в def lookups
            return queryset.filter(rating__lt=40)                                       # применяется фильтр из ОРМ
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '>= 80':
            return queryset.filter(rating__gte=80)
        return queryset


@admin.register(Movie)                                                                  # за классом админ указываем клас MovieAdmin
class MovieAdmin(admin.ModelAdmin):                                                     # класс обычно называют по названию модели + Admin
    list_display = ['name', 'rating', 'currency', 'year',  'budget', 'rating_status']   # перечисляем строками поля из класса Movie, 0й лемент будет ссылкой
    list_editable = ['rating', 'currency', 'year']                                      # перечисляем поля, которые можно редактировать из таблицы, поле 'name' нельзя указывать тк оно будет ссылкой
    ordering = ['rating', '-year']                                                      # сортировка, по рейтингу первостепенная, по году второстепенная
    list_per_page = 15                                                                  # сколько записей отображается на 1й странице
    actions = ['set_dollars', 'set_euro', 'set_rubles']                                 # добавили действия
    search_fields = ['name__endswith', 'rating']                                        # добавили фильтр по и мени и рейтингу
    list_filter = ['name', 'currency', RatingFilter]

    #fields = ['name', 'rating', 'year']                                                 # поля в создании и редактировании "карточки", отображается в том порядке как и в списке
    exclude = []                                                         # ротивоположный аргумент fields, сли список пустой, то выводит все поля, если добавить, то исключает их из видимсти
    #readonly_fields = ['rating']                                                         # перечисляем поля, которые запретщаем изменять - только чтение
    prepopulated_fields = {'slug': ('name', )}                                          # теперь при заполнении поля name будет автоматически заполняться поле slug в соответствующем формате. так же можно будет в ручную редактировать поле slug и если мы добавим что-то что не соответствует формату slug то джанго будет ругаться




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
            f'Было обновлено {count_update} записей'                                    # если тип сообщения не указывать, то будет стандартный INFO
        )

    @admin.action(description='Установить валюту в рубли')
    def set_rubles(self, request, qs: QuerySet):
        qs.update(currency=Movie.RUB)

        self.message_user(request, 'изменили валюту в рубли', messages.ERROR)           # тип сообщения ERROR
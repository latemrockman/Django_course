from django.contrib import admin, messages
from .models import Movie, Director, Actor, DressingRoom
from django.db.models import QuerySet



# Register your models here.

#admin.site.register(DressingRoom)

class OldStatusFilter(admin.SimpleListFilter):
    title = 'Фильтрация по возрастному статусу'
    parameter_name = 'old_status'

    def lookups(self, request, model_admin):
        return [
            ('младше 40', 'Молодой'),
            ('от 40 до 50', 'Средний возраст'),
            ('от 50 до 60', 'Старый'),
            ('старше 60', 'Очень старый'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == 'младше 40':
            return queryset.filter(age__lt=40)
        if self.value() == 'от 40 до 50':
            return queryset.filter(age__gte=40).filter(age__lt=50)
        if self.value() == 'от 50 до 60':
            return queryset.filter(age__gte=50).filter(age__lt=60)
        if self.value() == 'старше 60':
            return queryset.filter(age__gt=60)

        return queryset

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

class SkillFilter(admin.SimpleListFilter):
    title = 'Опыт съемок'
    parameter_name = 'skill'

    def lookups(self, request, model_admin):
        return [
            ('меньше 3', 'Junior'),
            ('от 3 до 5', 'Middle'),
            ('от 5 до 10', 'Senior'),
            ('больше 10', 'Team Leed'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'меньше 3':
            return queryset.filter(count_movie__lt=3)
        elif self.value() == 'от 3 до 5':
            return queryset.filter(count_movie__gte=3).filter(count_movie__lt=5)
        elif self.value() == 'от 5 до 10':
            return queryset.filter(count_movie__gte=5).filter(count_movie__lt=10)
        elif self.value() == 'больше 10':
            return queryset.filter(count_movie__gte=10)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


@admin.register(Director)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'age', 'old_status', 'director_email', 'country', 'slug']
    list_editable = ['director_email', 'country', 'age']
    ordering = ['first_name']
    list_per_page = 15
    actions = ['set_italy', 'set_spain', 'set_france', 'set_germany', 'set_hello']
    prepopulated_fields = {'slug': ('last_name', 'first_name', )}
    search_fields = ['first_name__endswith', 'last_name__startswith']
    list_filter = ['first_name', 'country', OldStatusFilter]
    fields = ['first_name', 'last_name', 'director_email', 'country', 'slug']
    #readonly_fields = ['']


    @admin.action(description='Заменить имя на "Hello"')                             # декоратор указывает, что это действие в админке + название
    def set_hello(self, request, qs: QuerySet):
        qs.update(first_name=Director.HI)

        self.message_user(request, 'заменили имя на "Hello"', messages.WARNING)

    @admin.action(description='Установить страну Италия')                             # декоратор указывает, что это действие в админке + название
    def set_italy(self, request, qs: QuerySet):
        qs.update(country=Director.IT)                                                   # update - метод класса Queryset, установить значение currency Movie.USD

        self.message_user(request, 'изменили страну', messages.WARNING)             # тип сообщения WARNING

    @admin.action(description='Установить страну Испания')                             # декоратор указывает, что это действие в админке + название
    def set_spain(self, request, qs: QuerySet):
        qs.update(country=Director.IS)                                                   # update - метод класса Queryset, установить значение currency Movie.USD

        self.message_user(request, 'изменили страну', messages.INFO)             # тип сообщения INFO


    @admin.action(description='Установить страну Франция')                             # декоратор указывает, что это действие в админке + название
    def set_france(self, request, qs: QuerySet):
        qs.update(country=Director.FR)                                                   # update - метод класса Queryset, установить значение currency Movie.USD

        self.message_user(request, 'изменили страну', messages.ERROR)             # тип сообщения INFO

    @admin.action(description='Установить страну Германия')                             # декоратор указывает, что это действие в админке + название
    def set_germany(self, request, qs: QuerySet):
        qs.update(country=Director.GE)                                                   # update - метод класса Queryset, установить значение currency Movie.USD

        self.message_user(request, 'изменили страну', messages.SUCCESS)             # тип сообщения INFO



    @admin.display(description='Возастной статус')
    def old_status(self, moviemaker: Director):
        if moviemaker.age < 40:
            return 'Молодой'
        elif moviemaker.age >= 40 and moviemaker.age < 50:
            return 'Средний возраст'
        elif moviemaker.age >= 50 and moviemaker.age < 60:
            return 'Старый'
        elif moviemaker.age >= 60:
            return 'Очень старый'

@admin.register(Actor)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'genre', 'gender', 'age', 'old_status', 'count_movie', 'slug', 'dressing']
    list_editable = ['age', 'genre', 'count_movie']
    ordering = ['first_name']
    list_per_page = 15
    actions = ['set_comedy']
    prepopulated_fields = {'slug': ('last_name', 'first_name')}
    search_fields = ['first_name__endswith', 'last_name__startswith']
    list_filter = ['gender', 'genre', OldStatusFilter, SkillFilter]
    fields = []
    readonly_fields = []







    @admin.action(description='Установиь жанр Комедия')
    def set_comedy(self, request, qs: QuerySet):
        qs.update(genre=Actor.COMEDY)

        self.message_user(request, 'установили жанр Комедия', messages.INFO)

    @admin.display(description='Возастной статус')
    def old_status(self, moviemaker: Director):
        if moviemaker.age < 40:
            return 'Молодой'
        elif moviemaker.age >= 40 and moviemaker.age < 50:
            return 'Средний возраст'
        elif moviemaker.age >= 50 and moviemaker.age < 60:
            return 'Старый'
        elif moviemaker.age >= 60:
            return 'Очень старый'

@admin.register(Movie)                                                                  # за классом админ указываем клас MovieAdmin
class MovieAdmin(admin.ModelAdmin):                                                     # класс обычно называют по названию модели + Admin
    list_display = ['name', 'rating', 'director', 'year',  'budget', 'rating_status']   # перечисляем строками поля из класса Movie, 0й лемент будет ссылкой
    list_editable = ['rating', 'director', 'year']                                      # перечисляем поля, которые можно редактировать из таблицы, поле 'name' нельзя указывать тк оно будет ссылкой
    ordering = ['rating', '-year']                                                      # сортировка, по рейтингу первостепенная, по году второстепенная
    list_per_page = 15                                                                  # сколько записей отображается на 1й странице
    actions = ['set_dollars', 'set_euro', 'set_rubles']                                 # добавили действия
    search_fields = ['name__endswith', 'rating']                                        # добавили фильтр по и мени и рейтингу
    list_filter = ['name', 'currency', RatingFilter]

    #fields = ['name', 'rating', 'year']                                                # поля в создании и редактировании "карточки", отображается в том порядке как и в списке
    exclude = []                                                                        # ротивоположный аргумент fields, сли список пустой, то выводит все поля, если добавить, то исключает их из видимсти
    #readonly_fields = ['rating']                                                       # перечисляем поля, которые запретщаем изменять - только чтение
    prepopulated_fields = {'slug': ('name', )}                                          # теперь при заполнении поля name будет автоматически заполняться поле slug в соответствующем формате. так же можно будет в ручную редактировать поле slug и если мы добавим что-то что не соответствует формату slug то джанго будет ругаться

    filter_horizontal = ['actors']                                                      # добавляем горизонтальный фильтр
    #filter_vertical = ['actors']                                                       # такой же фильтр, только виджет располагается снизу, а горизонтальный сбоку

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
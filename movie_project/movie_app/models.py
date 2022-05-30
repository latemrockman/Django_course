from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from . translit import text2translit



# Create your models here.

class Director(models.Model):

    RU = 'RU'
    IT = 'IT'
    IS = 'IS'
    FR = 'FR'
    GE = 'GE'

    HI = 'Hello'

    COUNTRIES = [
        ('RU', 'Россия'),
        ('IT', 'Италия'),
        ('IS', 'Испания'),
        ('FR', 'Франция'),
        ('GE', 'Германия')
    ]


    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()
    slug = models.SlugField(default='', null=False, db_index=True)
    country = models.CharField(max_length=10, choices=COUNTRIES,
                              default=RU)
    age = models.IntegerField(default=30, null=False, validators=[MinValueValidator(1), MaxValueValidator(150)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        translit_slug = text2translit(f'{self.last_name} {self.first_name}')
        self.slug = slugify(translit_slug)
        super(Director, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('director-details', args=[self.slug])
        #return f'/director/{self.slug}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):  # таблица с актерами
    MALE = 'M'  # переменне М и Ж
    FEMALE = 'F'

    GENDERS = [  # список кортежей М и Ж
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    ]

    TRILLER = 'T'
    COMEDY = 'C'
    DRAMMA = 'D'
    TRAGEDY = 'T'

    GENRE = [
        (TRILLER, 'Триллер'),
        (COMEDY, 'Комедия'),
        (DRAMMA, 'Драмма'),
        (TRAGEDY, 'Трагедия'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS,
                              default=MALE)  # колонка ПОЛ, max_length - максимальная длина 1 тк 'F' или 'M', choices - передаем список кортежей с вариантами значений, default - начение по умолчанию МУЖЧИНА
    slug = models.SlugField(default='', null=False, db_index=True)
    age = models.IntegerField(default=25, null=False, validators=[MinValueValidator(1), MaxValueValidator(150)])
    count_movie = models.IntegerField(default=0, null=False, validators=[MinValueValidator(0)])
    genre = models.CharField(max_length=1, choices=GENRE,
                              default=TRILLER)  # колонка ПОЛ, max_length - максимальная длина 1 тк 'F' или 'M', choices - передаем список кортежей с вариантами значений, default - начение по умолчанию МУЖЧИНА

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        translit_slug = text2translit(self.full_name())
        self.slug = slugify(translit_slug)
        super(Actor, self).save(*args, **kwargs)


    def get_url(self):
        return reverse('actor-details', args=[self.slug])

    def __str__(self):
        if self.gender == self.MALE:  # если gender == MALE, обращаемся через self.
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'

    # def get_url(self):
    #    return reverse('actor-details', args=[self.id])


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCYL_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles')
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(blank=True, validators=[MinValueValidator(1),
                                                         MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1800),
                                                                  MaxValueValidator(2022)])
    budget = models.IntegerField(default=10000000, blank=True, validators=[MinValueValidator(0)])
    currency = models.CharField(max_length=3, choices=CURRENCYL_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        translit_slug = text2translit(self.name)
        self.slug = slugify(translit_slug)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-details', args=[self.slug])
        #return f'movie/{self.slug}'

    def __str__(self):
        return f'{self.name} - {self.rating}%'

# from movie_app.models import Movie

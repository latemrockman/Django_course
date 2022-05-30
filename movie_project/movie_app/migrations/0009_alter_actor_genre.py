# Generated by Django 4.0.4 on 2022-05-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_actor_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='genre',
            field=models.CharField(choices=[('T', 'Триллер'), ('C', 'Комедия'), ('D', 'Драмма'), ('T', 'Трагедия')], default='T', max_length=1),
        ),
    ]

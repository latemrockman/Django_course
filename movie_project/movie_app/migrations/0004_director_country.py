# Generated by Django 4.0.4 on 2022-05-30 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_actor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='country',
            field=models.CharField(choices=[('RU', 'Россия'), ('IT', 'Италия'), ('IS', 'Испания'), ('FR', 'Франция'), ('GE', 'Германия')], default='RU', max_length=10),
        ),
    ]

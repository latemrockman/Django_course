from django import forms
from .models import Feedback



#class FeedbackForm(forms.Form):                             # обязательно наслудуется от forms.Form
#    messages = {
#        'max_length': 'Слишком много символов',
#        'min_length': 'Слишком мало символов',
#        'required': 'Укажите хотябы 1 символ'
#    }
#    name = forms.CharField(label='Имя',                    # label перед полем ввода
#                           max_length=7,                   # максимальная длина
#                           min_length=2,                   # минимальая длина
#                           error_messages=messages)        # стандартные сообщения об ошибке можно заменить, принимает словарь
#
#    surname = forms.CharField(label="Фамилия")
#    rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=100, help_text="Задайте райтинг", disabled=False, show_hidden_initial=False)
#
#
#    atrib = {
#        'rows': 5,
#        'cols': 40
#    }
#    feedback = forms.CharField(label='Отзыв',
#                               widget=forms.Textarea(attrs=atrib))      # widget по умолчанию равен TextInut, меняем на Textarea
#                                                                        # у виджета Textarea добавляем атрибуты через attrs (принимает словарь со значениями)


class FeedbackForm(forms.ModelForm):                                        # наследуем от forms.ModelForm
    class Meta:                                                             # добавляем класс Meta
        model = Feedback                                                    # указываем Модель на основе которой делаем форму
        #fields = ['surname', 'rating']                              # перечисляем поля, которые нужны
        fields = '__all__'                                                  # выбираем все поля
        #exclude = ['feedback']                                                # перечисляем поля, которые нужно исключить

        labels = {                                                          # в labels перечисляем какие подписи будут к полям ввода
            'name'      : 'Имя',
            'surname'   : 'Фамилия',
            'feedback'  : 'Отзыв',
            'rating'    : 'Рейтинг'
        }

        error_message = {
            'name': {
                'max_length': 'слишком много символов',
                'min_length': 'слишком мало символов',
                'required': 'поле не должно быть пустым!!!'
            },
            'surname': {
                'max_length': 'слишком много символов',
                'min_length': 'слишком мало символов',
                'required': 'поле не должно быть пустым!!!'
            },
            'rating': {
                'max_length': 'слишком большое число',
                'min_length': 'слишком маленькое число',
                'required': 'поле не должно быть пустым!!!'
            }
        }





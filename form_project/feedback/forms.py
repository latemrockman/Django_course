from django import forms



class FeedbackForm(forms.Form):                             # обязательно наслудуется от forms.Form
    name = forms.CharField()                                # аналогично отрибуту name в теге
    surname = forms.CharField()

    atrib = {
        'rows': 5,
        'cols': 40
    }



    feedback = forms.CharField(widget=forms.Textarea(attrs=atrib))      # widget по умолчанию равен TextInut, меняем на Textarea
                                                                        # у виджета Textarea добавляем атрибуты через attrs (принимает словарь со значениями)
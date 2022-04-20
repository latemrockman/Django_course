from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split')          # навешиваем декоратор, чтобы функция стала фильтром. name - название фильтра, можно придумать свой
@stringfilter
def split(value, key=' '):              # значение, которое будет разбиваться по какому-то знаку и ключ(знак)
    return value.split(key)
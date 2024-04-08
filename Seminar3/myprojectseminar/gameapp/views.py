from random import randint, choice

from django.http import HttpResponse
from django.shortcuts import render

from .models import Coin


def index(request):
    context = {'name': 'Vitaly',
               'age': 31,
               'city': 'Moscow',
               'country': 'Russia',
               }
    return render(request, 'gameapp/index.html', context=context)


def two_index(request):
    return render(request, 'gameapp/two_index.html')


# def coin(request, count=5):
#     result = []
#     for i in range(count):
#         value = choice(['Орёл', 'Решка'])
#         result.append(value)
#
#     context = {'game_name': 'Орёл или решка',
#                'value': result}
#     return render(request, 'gameapp/game.html', context=context)

def coin(request, count):
    name = 'Орёл или решка'
    value = ''
    for i in range(count):
        value += choice(['Орёл', 'Решка'])
        if i < count - 1:
            value += ', '
    context = {'game_name': name,
               'value': value}

    return render(request, 'gameapp/game.html', context=context)


def kub(request, count):
    name = 'Кубик'
    value = ''
    for i in range(count):
        value += str(randint(1, 7))
        if i < count - 1:
            value += ', '
    context = {'game_name': name,
               'value': value}
    return render(request, 'gameapp/game.html', context=context)


def numbers(request, count):
    name = 'Числа'
    value = ''
    for i in range(count):
        value += str(randint(1, 7))
        if i < count - 1:
            value += ', '
    context = {'game_name': name,
               'value': value}
    return render(request, 'gameapp/game.html', context=context)


def coin_values(request):
    value = Coin.values()
    print(value)
    lst = []
    for i in value:
        print(i)
        lst.append(i.site)
    return HttpResponse(lst)

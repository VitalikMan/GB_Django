from random import randint, choice

from django.http import HttpResponse

from .models import Coin


def index(request):
    return HttpResponse("Hello, world!")


def coin(request):
    site = choice(['Орёл', 'Решка'])
    arg_ = Coin(site=site)
    arg_.save()
    return HttpResponse(str(site))


def kub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))


def coin_values(request):
    value = Coin.values()
    print(value)
    lst = []
    for i in value:
        print(i)
        lst.append(i.site)
    return HttpResponse(lst)

from random import randint, choice
from django.http import HttpResponse
from django.shortcuts import render
from .models import Coin
from .forms import GameCoin


def main(request):
    context = {
        "title": "Мой сайт",
        "index": "Приветствую на моём сайте!",
        "message1": "Это главная страница",
        "message2": "Базовый шаблон проекта",
    }
    return render(request, "gameapp/base.html", context=context)


def index(request):
    context = {
        "title": "О себе",
        "name": "Vitaly",
        "age": 31,
        "city": "Moscow",
        "country": "Russia",
    }
    return render(request, "gameapp/index.html", context=context)


def two_index(request):
    return render(request, "gameapp/two_index.html")


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
    name = "Орёл или решка"
    value = ""
    for i in range(count):
        value += choice(["Орёл", "Решка"])
        if i < count - 1:
            value += ", "
    context = {"game_name": name, "value": value}

    return render(request, "gameapp/game.html", context=context)


def kub(request, count):
    name = "Кубик"
    value = ""
    for i in range(count):
        value += str(randint(1, 7))
        if i < count - 1:
            value += ", "
    context = {"game_name": name, "value": value}
    return render(request, "gameapp/game.html", context=context)


def numbers(request, count):
    name = "Числа"
    value = ""
    for i in range(count):
        value += str(randint(1, 7))
        if i < count - 1:
            value += ", "
    context = {"game_name": name, "value": value}
    return render(request, "gameapp/game.html", context=context)


def coin_values(request):
    value = Coin.values()
    print(value)
    lst = []
    for i in value:
        print(i)
        lst.append(i.site)
    return HttpResponse(lst)


def game_choice(request):
    if request.method == "POST":
        form = GameCoin(request.POST)
        if form.is_valid():
            game = form.cleaned_data["game"]
            size = form.cleaned_data["size"]
            if game == "coin":
                return coin(request, count=size)
            elif game == "kub":
                return kub(request, count=size)
            elif game == "numbers":
                return numbers(request, count=size)
    else:
        form = GameCoin()
    return render(request, "gameapp/game_two.html", {"form": form})

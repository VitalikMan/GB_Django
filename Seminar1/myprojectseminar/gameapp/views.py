from django.shortcuts import render

from django.http import HttpResponse
from random import randint, choice


def index(request):
    return HttpResponse("Hello, world!")


def heads_and_tails(request):
    return HttpResponse(choice(['Орёл', 'Решка']))


def kub(request):
    return HttpResponse(str(randint(1, 7)))


def numbers(request):
    return HttpResponse(str(randint(0, 1000)))
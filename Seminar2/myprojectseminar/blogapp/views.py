from django.http import HttpResponse

from .models import Author


def index(request):
    return HttpResponse("Hello, world!")


def authors(request):
    for i in range(101):
        author = Author(name=f'Johnny {i}',
                        surname=f'Depp {i}',
                        email=f'depp@gmail.com {i}',
                        biography=f"I am Johnny Depp. I am students of GB {i}",
                        birthday=f'2024-04-06')
        author.save()
    return HttpResponse("Author")

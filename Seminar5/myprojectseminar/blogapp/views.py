from django.http import HttpResponse
from django.shortcuts import render
from .models import Author
from .forms import AuthorForms


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


def post_author(request):
    if request.method == 'POST':
        form = AuthorForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['biography']
            birthday = form.cleaned_data['birthday']
            author = Author(name=name,
                            surname=surname,
                            email=email,
                            biography=biography,
                            birthday=birthday)
            author.save()
            return render(request, 'blogapp/post_author.html', {'answer': 'Автор добавлен!'})
    else:
        form = AuthorForms()
    return render(request, 'blogapp/post_author.html', {'form': form})


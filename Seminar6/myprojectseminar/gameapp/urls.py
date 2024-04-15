"""
URL configuration for myprojectseminar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import index, coin, kub, numbers, coin_values, two_index, game_choice

urlpatterns = [
    path('', index, name='index'),
    path('two_index', two_index, name='two_index'),
    path('coin/<int:count>', coin, name='coin'),
    path('kub/<int:count>', kub, name='kub'),
    path('numbers/<int:count>', numbers, name='numbers'),
    path('coin_values/', coin_values, name='coin_values'),
    path('game_choice/', game_choice, name='game_choice'),
]

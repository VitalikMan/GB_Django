"""
URL configuration for HomeWork project.

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
from . views import main, mysite, fake_db, customer_ordered_items


urlpatterns = [
    path('', main, name='main'),
    path('mysite/', mysite, name='mysite'),
    path('fake_db/', fake_db, name='fake_db'),
    path('ordered_items/<int:period>', customer_ordered_items, name='customer_ordered_items'),
]
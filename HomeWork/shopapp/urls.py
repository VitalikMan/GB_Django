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
from .views import (
    mysite,
    fake_db,
    customer_ordered_items,
    create_product,
    all_products,
    product_detail,
    edit_product,
)

urlpatterns = [
    path("", mysite, name="mysite"),
    path("fake_db/", fake_db, name="fake_db"),
    path(
        "ordered_items/<int:period>",
        customer_ordered_items,
        name="customer_ordered_items",
    ),
    path("create_product/", create_product, name="create_product"),
    path("all_products/", all_products, name="all_products"),
    path("product_detail/<int:product_id>", product_detail, name="product_detail"),
    path("edit_product/<int:product_id>", edit_product, name="edit_product"),
]

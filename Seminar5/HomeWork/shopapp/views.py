from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Customer, Product, Order
from random import choice, randint
from datetime import datetime, timedelta
from django.utils.timezone import now
from .forms import ProductForm
import logging

logger = logging.getLogger(__name__)


def mysite(request):
    mysite_html = (
        "<h2>Добро пожаловать в магазин Интерьерных Решений!</h2>"
        "<p>Добро пожаловать в наш магазин Интерьерных Решений!</p>"
        "<p>У нас вы найдете широкий ассортимент стильной мебели, аксессуаров и декора для вашего дома.</p>"
        "<p>Позвольте нам помочь вам создать уют и гармонию в вашем интерьере.</p>"
        "<p>Индивидуальный подход к каждому клиенту и быстрая доставка по всей России гарантированы.</p>"
        "<p>Откройте для себя новые возможности для вашего дома с нами!</p>"
    )
    return HttpResponse(mysite_html)


def fake_db(request):
    streets = ["Гоголя", "Советская", "Пушкина", "Лермонтова", "Шелеста", "Ленина"]
    for i in range(10):
        street = choice(streets)
        random_date = timezone.now() - timedelta(days=randint(1, 365))
        formatted_date = random_date.strftime("%Y-%m-%d")
        customer = Customer.objects.create(
            name=f"Петя_{i}",
            email=f"petya_{i}@mail.ru",
            phone_number=f"+7(555)-555-{randint(i, 100)}-{randint(i, 100)}",
            address=f"ул. {street}, д. {randint(1, 200)}, кв. {randint(1, 150)}",
            registration_date=formatted_date,
        )

        for j in range(randint(1, 5)):  # Каждый клиент делает от 1 до 5 заказов
            product = Product.objects.create(
                name=f"Продукт_{i}_{j}",
                description=f"Описание продукта_{i}_{j}",
                price=(i * 123.45) + (j * 10),  # Уникальная цена для каждого продукта
                quantity=randint(1, 10),
                date_added=random_date
                + timedelta(
                    days=randint(1, 30)
                ),  # Дата добавления отличается от даты заказа
            )
            order = Order.objects.create(
                customer=customer,
                total_amount=product.price,
                order_date=product.date_added,
            )
            order.products.add(product)  # Добавление продукта к заказу

            # Добавление продукта в связанные поля модели Customer
            if (timezone.now() - product.date_added).days <= 7:
                customer.ordered_items_last_week.add(product)
            if (timezone.now() - product.date_added).days <= 30:
                customer.ordered_items_last_month.add(product)
            if (timezone.now() - product.date_added).days <= 365:
                customer.ordered_items_last_year.add(product)

    return HttpResponse("Добавлено 10 клиентов с их заказами")


def customer_ordered_items(request, period):
    customers = Customer.objects.all()
    for customer in customers:
        ordered_items = get_ordered_items_within_period(customer, period)
        customer.ordered_items = ordered_items

    context = {"customers": customers, "period": period}
    return render(request, "shopapp/ordered_items.html", context)


def get_ordered_items_within_period(customer, period_days):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=period_days)

    ordered_items = set()
    orders = Order.objects.filter(
        customer=customer, order_date__range=(start_date, end_date)
    )
    for order in orders:
        ordered_items.update(order.products.all())  # Получение всех продуктов из заказа

    return ordered_items


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                price=form.cleaned_data["price"],
                quantity=form.cleaned_data["quantity"],
                image=form.cleaned_data["image"],
                date_added=now(),
            )
            logger.info(
                f"Получили {product.name=}, {product.description=}, {product.price=},"
                f"{product.quantity=}, {product.image=}."
            )
            product.save()
            context = {
                "answer": "Товар успешно добавлен!",
                "error": "Что-то пошло не так. Повторите еще раз!",
            }
            return render(request, "shopapp/create.html", context)
    else:
        form = ProductForm()
    context = {"form": form, "title": "Форма создания нового товара"}
    return render(request, "shopapp/create.html", context)


def all_products(request):
    # Получаем все продукты из базы данных
    products = Product.objects.all()
    # Передаем список продуктов в контекст шаблона
    context = {"products": products, "title": "Все товары"}
    # Отображаем шаблон со списком продуктов
    return render(request, "shopapp/all_products.html", context)


def product_detail(request, product_id):
    # Получаем экземпляр продукта по его ID или возвращаем 404, если продукт не найден
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product, "title": "Детали продукта"}
    return render(request, "shopapp/product_detail.html", context)


def edit_product(request, product_id):
    # Получаем экземпляр продукта по его ID или возвращаем 404, если продукт не найден
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        # Заполняем форму данными из POST-запроса и указываем экземпляр продукта для редактирования
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            # Сохраняем отредактированный продукт
            form.save()
            # Перенаправляем пользователя на страницу с информацией о продукте
            return redirect("product_detail", product_id=product.id)
    else:
        # Если это GET-запрос, создаем форму, заполняя ее данными текущего продукта
        form = ProductForm(instance=product)

    # Отображаем шаблон редактирования продукта с формой
    context = {"form": form, "product": product, "title": "Редактирование продукта"}
    return render(request, "shopapp/edit.html", context)

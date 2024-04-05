from datetime import datetime, timedelta
from django.http import HttpResponse
from random import randint, choice, random, uniform

from .models import Customer, Order, Product


def main(request):
    main_html = ("<h1>Страница описания моего второго домашнего задания по Django</h1>"
                 "<h2>Создайте три модели Django: клиент, товар и заказ.</h2>"
                 "<p>Клиент может иметь несколько заказов.</p>"
                 "<p>Заказ может содержать несколько товаров.</p>"
                 "<p>Товар может входить в несколько заказов.</p>"
                 "<h4> Модель 'Клиенты':</h4>"
                 "<p> Поля модели 'Клиент':</p>"
                 "<p>— имя клиента</p>"
                 "<p>— электронная почта клиента</p>"
                 "<p>— номер телефона клиента</p>"
                 "<p>— адрес клиента</p>"
                 "<p>— дата регистрации клиента</p>"
                 "<h4> Модель 'Товары':</h4>"
                 "<p> Поля модели 'Товар':</p>"
                 "<p>— название товара</p>"
                 "<p>— описание товара</p>"
                 "<p>— цена товара</p>"
                 "<p>— количество товара</p>"
                 "<p>— дата добавления товара</p>"
                 "<h4> Модель 'Заказы':</h4>"
                 "<p> Поля модели 'Заказ':</p>"
                 "<p>— связь с моделью 'Клиент', указывает на клиента, сделавшего заказ</p>"
                 "<p>— связь с моделью 'Товар', указывает на товары, входящие в заказ</p>"
                 "<p>— общая сумма заказа</p>"
                 "<p>— дата оформления заказа</p>"
                 
                 "<p>— Главная -> http://127.0.0.1:8000/shop/mysite/</p>"
                 "<p>— Фейковая база данных -> http://127.0.0.1:8000/shop/fake_db/</p>")
    return HttpResponse(main_html)


def mysite(request):
    mysite_html = ("<h2>Добро пожаловать в магазин Интерьерных Решений!</h2>"
                   "<p>Добро пожаловать в наш магазин Интерьерных Решений!</p>"
                   "<p>У нас вы найдете широкий ассортимент стильной мебели, аксессуаров и декора для вашего дома.</p>"
                   "<p>Позвольте нам помочь вам создать уют и гармонию в вашем интерьере.</p>"
                   "<p>Индивидуальный подход к каждому клиенту и быстрая доставка по всей России гарантированы.</p>"
                   "<p>Откройте для себя новые возможности для вашего дома с нами!</p>")
    return HttpResponse(mysite_html)


def fake_db(request):
    street = choice(['Гоголя', 'Советская', 'Пушкина',
                     'Лермонтова', 'Шелеста', 'Ленина'])
    for i in range(10):
        random_date = datetime.now() - timedelta(days=randint(1, 365))
        formatted_date = random_date.strftime('%Y-%m-%d')
        customer = Customer(name=f'Петя_{i}',
                            email=f'petya_{i}@mail.ru',
                            phone_number=f'+7(555)-555-{randint(i, 100)}-{randint(i, 100)}',
                            address=f'ул. {street}, д. {randint(1, 200)}, кв. {randint(1, 150)}',
                            registration_date=f'{formatted_date}')
        customer.save()

        product = Product(name=f'Продукт_{i}',
                          description=f'Описание продукта_{i}',
                          price=i * 123.45,
                          quantity=randint(1, 10),
                          date_added=datetime.now())
        product.save()

        order = Order(customer=customer,
                      order_date=product.date_added,
                      total_amount=product.price)
        order.save()

    return HttpResponse("Добавлено 10 клиентов с их заказами")

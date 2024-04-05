# �������:
# �������� ��� ������ Django:
#     � ������,
#     � �����,
#     � �����.
#
# ������ ����� ����� ��������� �������.
# ����� ����� ��������� ��������� �������.
# ����� ����� ������� � ��������� �������.
#
# ���� ������ �������:
#     � ��� �������,
#     � ����������� ����� �������,
#     � ����� �������� �������,
#     � ����� �������,
#     � ���� ����������� �������.
#
# ���� ������ ������:
#     � �������� ������,
#     � �������� ������,
#     � ���� ������,
#     � ���������� ������,
#     � ���� ���������� ������.
#
# ���� ������ ������:
#     � ����� � ������� �������, ��������� �� �������, ���������� �����,
#     � ����� � ������� ������, ��������� �� ������, �������� � �����,
#     � ����� ����� ������,
#     � ���� ���������� ������.
#
# �������� ��������� ������� CRUD ��� ������ � �������� �� �������. ��� �� ������ ������ ��������� � ����� ��
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    registration_date = models.DateField()

    def __str__(self):
        return f'{self.name} {self.phone_number}'


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField()

    def __str__(self):
        return f'{self.name} {self.description} {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} {self.order_date} {self.total_amount}'

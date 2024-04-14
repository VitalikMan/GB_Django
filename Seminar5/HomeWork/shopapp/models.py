from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateTimeField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.name} {self.description} {self.price}'


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    registration_date = models.DateField()
    ordered_items_last_week = models.ManyToManyField(Product, related_name='ordered_items_last_week')
    ordered_items_last_month = models.ManyToManyField(Product, related_name='ordered_items_last_month')
    ordered_items_last_year = models.ManyToManyField(Product, related_name='ordered_items_last_year')

    def __str__(self):
        return f'{self.name} {self.phone_number}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} {self.order_date} {self.total_amount}'

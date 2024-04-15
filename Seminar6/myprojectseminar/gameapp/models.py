from django.db import models
from django.utils import timezone

# Задание:
# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним броскам монеты.
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.


class Coin(models.Model):
    time = models.DateTimeField(default=timezone.now)
    site = models.CharField(max_length=10)

    @staticmethod
    def values():
        value = Coin.objects.order_by('-time')[:5]
        # print(value)
        return value

    def __str__(self):
        return f'time: {self.time}, site: {self.site}'

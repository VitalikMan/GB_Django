# Задание 3:
# Создайте модель Автор. Модель должна содержать
# следующие поля:
# - имя до 100 символов
# - фамилия до 100 символов
# - почта
# - биография
# - день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname}'

from django.contrib import admin
from .models import Coin


class AdminCoin(admin.ModelAdmin):
    list_display = ("site",)


admin.site.register(Coin, AdminCoin)

from django.contrib import admin
from .models import Customer, Product, Order


class AdminCustomer(admin.ModelAdmin):
    # список отображаемых полей
    list_display = (
        "name",
        "email",
        "phone_number",
        "address",
        "registration_date",
    )
    # список фильтров
    list_filter = ("name", "address")
    # список доступных полей для поиска
    search_fields = ("name", "address")
    # запрещает редактировать поля при выборе просмотра информации об авторе
    readonly_fields = (
        "registration_date",
        "ordered_items_last_week",
        "ordered_items_last_month",
        "ordered_items_last_year",
    )
    fieldsets = [
        [
            "Общая информация",  # заголовок
            {
                "fields": (
                    "name",
                    "email",
                    "phone_number",
                    "address",
                    "registration_date",
                ),
                "classes": ("wide",),
            },
        ],
        [
            "Покупки",  # заголовок
            {
                "fields": (
                    "ordered_items_last_week",
                    "ordered_items_last_month",
                    "ordered_items_last_year",
                ),
                "classes": ("wide",),
            },
        ],
    ]


class AdminProduct(admin.ModelAdmin):
    # список отображаемых полей
    list_display = (
        "name",
        "description",
        "price",
        "quantity",
    )
    # список фильтров
    list_filter = ("name", "price")
    # список доступных полей для поиска
    search_fields = ("name", "description")
    # запрещает редактировать поля при выборе просмотра информации о продукте
    readonly_fields = ("date_added", "image")
    fieldsets = [
        [
            "Наименование",  # заголовок
            {
                "fields": ("name",),
                "classes": ("wide",),
            },
        ],
        [
            "Описание",  # заголовок
            {
                "fields": ("description",),
                "classes": ("wide",),
            },
        ],
        [
            "Цена",  # заголовок
            {
                "fields": ("price",),
                "classes": ("wide",),
            },
        ],
        [
            "Количество",  # заголовок
            {
                "fields": ("quantity",),
                "classes": ("wide",),
            },
        ],
        [
            "Изображение",  # заголовок
            {
                "fields": ("image",),
                "classes": ("wide",),
            },
        ],
        [
            "Дата добавления",  # заголовок
            {
                "fields": ("date_added",),
                "classes": ("wide",),
            },
        ],
    ]


class AdminOrder(admin.ModelAdmin):
    # список отображаемых полей
    list_display = (
        "customer",
        "total_amount",
        "order_date",
    )
    # список фильтров
    list_filter = ("customer", "products", "order_date")
    # список доступных полей для поиска
    search_fields = ("customer", "products", "order_date")
    # запрещает редактировать поля при выборе просмотра информации о заказе
    readonly_fields = (
        "customer",
        "products",
        "total_amount",
        "order_date",
    )
    fieldsets = [
        [
            "Данные о заказе",  # заголовок
            {
                "fields": (
                    "customer",
                    "products",
                    "total_amount",
                    "order_date",
                ),
                "classes": ("wide",),
            },
        ],
    ]


admin.site.register(Customer, AdminCustomer)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)

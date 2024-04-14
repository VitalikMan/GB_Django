from django.contrib import admin
from .models import Author


@admin.action(description="Тестовая активность")
def admintest(modeladmin, request, queryset):
    queryset.update(name="test")


class AdminAuthor(admin.ModelAdmin):
    # список отображаемых полей
    list_display = (
        "name",
        "surname",
        "email",
        "biography",
        "birthday",
    )
    # список фильтров
    list_filter = (
        "name",
        "surname",
        "email",
    )
    # список доступных полей для поиска
    search_fields = (
        "name",
        "surname",
        "email",
    )
    # # отображает список видимых полей при выборе просмотра информации об авторе
    # fields = (
    #     "name",
    #     "surname",
    #     "email",
    #     "biography",
    #     "birthday",
    # )
    # запрещает редактировать поля при выборе просмотра информации об авторе
    readonly_fields = (
        "email",
        "birthday",
    )

    fieldsets = [
        [
            "Тест",  # заголовок
            {
                "fields": (
                    "name",
                    "surname",
                    "email",
                ),
                "classes": ("wide",),
            },
        ],
        [
            "Тест 2",  # заголовок
            {
                "fields": (
                    "biography",
                    "birthday",
                ),
                "classes": ("wide",),
            },
        ],
    ]
    actions = [admintest]


admin.site.register(Author, AdminAuthor)

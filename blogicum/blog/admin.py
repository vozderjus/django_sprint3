from django.contrib import admin
from . import models


class BlogAdminSite(admin.AdminSite):
    site_header = "Блог"
    site_title = "Блог"


# Регистрация моделей
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "pub_date", "is_published")
    list_editable = ("is_published",)
    search_fields = ("title", "text")
    list_filter = ("pub_date", "is_published", "category", "location")


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published")
    list_editable = ("is_published",)
    search_fields = ("title",)


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published")
    list_editable = ("is_published",)
    search_fields = ("name",)

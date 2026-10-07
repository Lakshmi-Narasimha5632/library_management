from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre", "published_date", "created_at")
    search_fields = ("title", "author", "isbn", "genre")
    list_filter = ("genre", "published_date")

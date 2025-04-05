from django.contrib import admin

from authors.models import Author
from unfold.admin import ModelAdmin


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ['user__username', 'user__first_name', 'bio', 'gender']
    list_filter = ['gender']
    search_fields = ["user__first_name", "user__last_name", "user__username", 'bio']
from django.contrib import admin

from authors.models import Author
from unfold.admin import ModelAdmin



# Register your models here.


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = ['user__first_name', 'bio', 'gender']
    list_filter = ['gender']
    search_fields = ["user__first_name", "user__last_name", "user__username", 'bio']
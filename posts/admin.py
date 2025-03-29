from django.contrib import admin

from posts.models import Post, Comment

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.title = "Admin"

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


# Register your models here.

@admin.register(Post)
class AuthorAdmin(ModelAdmin):
    list_display = ['title', 'total_likes', 'author', 'created_at', 'updated_at']
    list_filter = ['author', 'created_at']
    search_fields = ['author__user__first_name', 'author__user__last_name']


@admin.register(Comment)
class GroupAdmin(ModelAdmin):
    pass
from django.urls import path
from .views import index, detail, delete, create, update

urlpatterns = [
    path('', index, name='index'),
    path('new', create, name='create'),
    path('<post_id>', detail, name='details'),
    path('<post_id>/delete', delete, name='delete'),
    path('<post_id>/edit', update, name='update'),
]
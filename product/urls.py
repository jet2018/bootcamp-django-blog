# url patterns

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('add/', views.AddProductView.as_view(), name='add_product'),
]
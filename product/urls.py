# url patterns

from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('add/', views.AddProductView.as_view(), name='add_product'),
    path('<int:pk>', views.ProductDetailsView.as_view(), name='details'),
    path('<int:pk>/edit', views.UpdateProductView.as_view(), name='update_product'),
    path('<int:pk>/delete', views.DeleteProductView.as_view(), name='delete_product'),
]
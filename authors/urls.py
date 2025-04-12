from django.urls import path

from authors.views import logout_user, signin, registration, AuthorListView

app_name = 'authors'

urlpatterns = [
    path('', AuthorListView.as_view(), name='index'),
    path('logout', logout_user, name='logout'),
    path('login', signin, name='login'),
    path('register', registration, name='register'),
]

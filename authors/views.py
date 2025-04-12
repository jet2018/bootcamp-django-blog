from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.db.models import Q
from django.views.generic import ListView

from authors.models import Author


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('posts:index')
    return redirect('posts:index')


def signin(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('username')
        password = request.POST.get('password')

        if not email_or_username or not password:
            messages.error(request, "Username and password are required")
        else:
            check_user = User.objects.filter(Q(username=email_or_username) | Q(email=email_or_username))
            if check_user.exists():
                user = check_user.get()
                authenticated = authenticate(username=user.username, password=password)
                if authenticated is not None:
                    messages.success(request, f"Welcome back {user.username}")
                    login(request, authenticated) # start session
                    return redirect('authors:index')
                else:
                    messages.error(request, "User not found")
            else:
                messages.error(request, "User not found")
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        create_password = request.POST.get("create_password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")

        if username is None or email is None or confirm_password is None or create_password is None or last_name is None or first_name is None:
            messages.error(request, "Please fill all form fields")
        elif create_password != confirm_password:
            messages.error(request, "Passwords did not match")
        else:
            try:
                User.objects.create_user(username=username, email=email, password=confirm_password, first_name=first_name, last_name=last_name)
                messages.success(request, f"User - {username} created successfully")
                return redirect('authors:login')
            except Exception as e:
                messages.error(request, e)

    return render(request, 'register.html')


# def authors(request):
#     author_list = Author.objects.all()
#     paginator = Paginator(author_list, 2)  # Show 25 contacts per page.
#
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'authors/index.html', {"page_obj": page_obj})


class AuthorListView(LoginRequiredMixin, ListView):
    template_name = 'authors/index.html'
    model = Author
    paginate_by = 2
    context_object_name = 'authors'

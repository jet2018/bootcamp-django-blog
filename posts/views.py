from django.shortcuts import render, get_object_or_404, redirect

from authors.models import Author
from posts.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, template_name='index.html', context={
        'title': 'Home Page',
        'content': 'Welcome to the home page of our blog!',
        'posts': posts,
    })


def detail(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    return render(request, template_name='detail.html', context={
        'title': f'Post {post_id}',
        'content': post.content,
        'post': post,
    })


def delete(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('posts:index')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = Author.objects.first()
    Post.objects.create(
        title=title,
        content=content,
        author=author,
    )
    return redirect('posts:index')


def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:index')
    return render(request, template_name='update.html', context={
        'title': f'Update Post {post_id}',
        'content': post.content,
        'post': post,
    })

# def random(request):
#     posts = Post.objects.filter().order_by('?')
#     return render(request, template_name='update.html', context={
#         'title': f'Update Post {post_id}',
#         'content': post.content,
#         'post': post,
#     })

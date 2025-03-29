from django.contrib.auth.models import User
from django.db import models

from authors.models import Author


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    bookmarks = models.ManyToManyField(User, related_name='bookmarks', blank=True)

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_bookmarks(self):
        return self.bookmarks.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    def __str__(self):
        return f"{self.user.username}"

    @property
    def total_likes(self):
        return self.likes.count()
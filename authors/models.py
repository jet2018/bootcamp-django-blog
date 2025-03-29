from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Author(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='authors_profiles', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=True, null=True)

    def __str__(self):
        return self.user.username


# trigger -- signals
@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
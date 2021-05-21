from django.contrib.auth.models import AbstractUser
from django.db import models


class BlogUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    phone_no = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + self.last_name

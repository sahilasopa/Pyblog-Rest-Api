from ckeditor.fields import RichTextField
from django.db import models

from accounts.models import BlogUser


class Blog(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blog = RichTextField()
    views = models.ManyToManyField(BlogUser, blank=True, related_name='Views')
    likes = models.ManyToManyField(BlogUser, blank=True, related_name='Likes')
    comments = models.CharField(blank=True, max_length=120)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

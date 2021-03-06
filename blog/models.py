from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import BlogUser


class Blog(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    blog = RichTextField()
    views = models.ManyToManyField(BlogUser, blank=True, related_name='Views')
    likes = models.ManyToManyField(BlogUser, blank=True, related_name='Likes')
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    @property
    def BlogPreview(self):
        return self.blog[:60]

    def get_absolute_url(self):
        return f'{self.id}'


class Comment(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name="blogUser")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blogs")
    comment = models.CharField(max_length=600)
    time_created = models.DateTimeField(auto_now_add=True, null=True)

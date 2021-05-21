# Generated by Django 3.2.3 on 2021-05-21 17:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='Views', to=settings.AUTH_USER_MODEL),
        ),
    ]

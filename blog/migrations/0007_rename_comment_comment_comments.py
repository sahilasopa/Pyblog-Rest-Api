# Generated by Django 3.2.3 on 2021-05-23 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comments',
        ),
    ]

from django.utils.html import strip_tags
from rest_framework.serializers import ModelSerializer

from blog.models import Blog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['blog'] = strip_tags(instance.blog)
        return data

from rest_framework import serializers

from accounts.serializers import UserSerializer
from blog.models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='blogs', many=True)
    user = UserSerializer()
    BlogPreview = serializers.CharField()
    get_absolute_url = serializers.CharField()

    class Meta:
        model = Blog
        fields = '__all__'

from rest_framework import serializers

from blog.models import Blog, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='blogs', many=True)

    class Meta:
        model = Blog
        fields = "__all__"

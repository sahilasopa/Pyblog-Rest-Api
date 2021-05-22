from rest_framework import serializers

from blog.models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

from rest_framework.serializers import ModelSerializer

from .models import BlogUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = BlogUser
        fields = 'username', 'first_name', 'last_name', 'email', 'phone_no'


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = BlogUser
        fields = 'id', 'username', 'first_name', 'last_name', 'email', 'phone_no'

from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Blog
from blog.serializers import BlogSerializer


@api_view((["GET"]))
def BlogsList(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

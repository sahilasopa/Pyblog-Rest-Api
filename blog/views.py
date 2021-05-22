import jwt
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from accounts.models import BlogUser
from blog.models import Blog
from blog.serializers import BlogSerializer


@api_view((["GET"]))
def BaseAPI(request):
    response = {
        "User List": "/accounts/users",
        "User Detail": "/accounts/user/<id>",
        "User Create": "/accounts/user/create",
        "User Login": "/accounts/login",
        "User Retrieve (Cookies)": "/accounts/user/retrieve",
        "User Logout": "/accounts/logout",
        "Blog List": "/blogs/list",
        "Blog Detail": "/blog/<id>",
        "Blog Create": "/blog/create",
        "Blog Update": "/blog/update/<id>",
        "Blog Delete": "/blog/delete/<id>",
    }
    return Response(response)


def RetrieveUserUsingCookies(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("UnAuthenticated")
    try:
        payload = jwt.decode(token, "secret", algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("UnAuthenticated")
    user = BlogUser.objects.get(id=payload['id'])
    return user


@api_view((["GET"]))
def BlogsList(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def BlogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(['GET', "POST"])
def BlogCreate(request):
    if request.method == "POST":
        user = RetrieveUserUsingCookies(request=request)
        request.data['user'] = user.id
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response("Create A Blog")


@api_view(['GET', "POST"])
def BlogUpdate(request, pk):
    blog = Blog.objects.get(id=pk)
    user = RetrieveUserUsingCookies(request=request)
    if user.id != blog.user.id:
        raise PermissionDenied("You Dont Have Permissions To Edit This Blog")
    serializer = BlogSerializer(blog)
    if request.method == "POST":
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response(serializer.data)


@api_view(["GET"])
def BlogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    user = RetrieveUserUsingCookies(request=request)
    if user.id != blog.user.id:
        raise PermissionDenied("You Dont Have Permissions To Delete This Blog")
    blog.delete()
    return Response("Successfully Deleted Blog")

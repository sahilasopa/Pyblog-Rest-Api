import datetime

import jwt
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .serializers import *


@api_view(["GET"])
def UsersList(request):
    users = BlogUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def UserDetail(request, pk):
    users = BlogUser.objects.get(id=pk)
    serializer = UserSerializer(users)
    return Response(serializer.data)


@api_view(["GET", "POST"])
def UserCreate(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response("Create User")


@api_view(["GET", "POST"])
def UserLogin(request):
    if request.method == "POST":
        username = request.data['username']
        password = request.data['password']
        user = BlogUser.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response
    return Response("Login")


@api_view(["GET"])
def RetrieveUserUsingCookies(request):
    if request.method == "GET":
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("UnAuthenticated")
        try:
            print(token)
            payload = jwt.decode(token, "secret", algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("UnAuthenticated")
        user = BlogUser.objects.get(id=payload['id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET', "POST"])
def UserLogout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

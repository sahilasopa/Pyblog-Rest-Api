from django.urls import path

from accounts import views

urlpatterns = [
    path('users', views.UsersList, name="usersList"),
    path('user/<int:pk>', views.UserDetail, name="userDetail"),
    path('user/create', views.UserCreate, name="userCreate"),
    path('user/login', views.UserLogin, name="userLogin"),
    path('user/retrieve', views.RetrieveUserUsingCookies, name="retrieve"),
    path('user/logout', views.UserLogout, name="logout"),
]

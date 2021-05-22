from django.urls.conf import path

from . import views

urlpatterns = [
    path("", views.BaseAPI, name="BaseAPI"),
    path("blogs/list", views.BlogsList, name="BlogList"),
    path("blog/create", views.BlogCreate, name="BlogCreate"),
    path("blog/<str:pk>", views.BlogDetail, name="BlogDetail"),
    path("blog/update/<str:pk>", views.BlogUpdate, name="BlogUpdate"),
    path("blog/delete/<str:pk>", views.BlogDelete, name="BlogDelete"),
]

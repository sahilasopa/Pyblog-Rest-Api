from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

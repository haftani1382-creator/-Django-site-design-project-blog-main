
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('' , include('pages.urls')) ,#www.ryan-blog.com
    path('posts/' , include('posts.urls')) ,#www.ryan-blog.com\posts\
    path('accounts/' , include('accounts.urls')) ,#www.ryan-blog.com\accounts\
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

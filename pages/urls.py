from django.urls import path

from . import views

urlpatterns=[
    path('' , views.index , name='index'), #www.ryan-blog.com\
    path('about' , views.about , name='about')#www.ryan-blog.com\about
]
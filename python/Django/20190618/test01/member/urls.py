from django.urls import path, re_path
from member.views import *
urlpatterns = [
    path('login/', login),
    path('index/', index),
    path('order/', order),
]
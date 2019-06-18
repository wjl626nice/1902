from django.urls import path, re_path
from sysAdmin import views
urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
]
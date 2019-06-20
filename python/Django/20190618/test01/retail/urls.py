from django.urls import path,re_path

from retail.views import *

app_name = 'retail'
urlpatterns = [
    path('login/', login, name='l')
]
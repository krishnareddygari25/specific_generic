from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[
    path('managamma/',managamma,name='managamma'),
    path('bhaskar/',bhaskar,name='bhaskar'),
]
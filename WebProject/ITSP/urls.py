
from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<str:pk>',views.singleteam,name='singleteam')
]

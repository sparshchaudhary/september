from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Gjob, name='Gjob'),
    path('gsearch', views.gsearch, name='gsearch'),
    path('<str:slug>', views.GjobPost, name='GjobPost')
]
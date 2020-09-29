from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.FinanceNews, name='FinanceNews'),
    path('<str:slug>', views.FinanceNewsPostPage, name='FinanceNewsPostPage')
]
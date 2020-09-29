from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Stock, name='Stock'),
    path('lasttrade', views.lasttrade, name='lasttrade'),
    path('ssearch', views.ssearch, name='ssearch'),
    path('<str:slug>', views.StockPost, name='StockPost')
]
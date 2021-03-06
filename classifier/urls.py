from django.contrib import admin
from django.urls import path, re_path, include

from classifier import views

urlpatterns = [
    path('start/<int:pk>', views.start, name='start'),
    path('start_all', views.start_all, name='start_all'),
    path('stop/<int:pk>', views.stop, name='stop'),
    path('stop_all', views.stop_all, name='stop_all'),
]

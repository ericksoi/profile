from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('calculator/home', views.post_list, name='post_list')
]
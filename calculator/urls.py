from django.conf.urls import url
from django.contrib import admin
from calculator import views
from django.urls import path, include


urlpatterns = [
    url('', views.HomePage.as_view()),
    url('home/', include('main.urls'))
]
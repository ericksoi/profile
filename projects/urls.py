from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.project_list, name='project_list'),
	path('calculator/', include('calculator.urls')),
	path('home/', include('main.urls')),
]
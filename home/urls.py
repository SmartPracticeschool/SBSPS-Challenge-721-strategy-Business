from django.urls import path
from . import views
from home.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.home1, name='home1'),
    path('home/', views.home, name='home')
]
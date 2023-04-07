from django.urls import re_path, path
from .views import index, route
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('route/', views.route, name='route'),
]
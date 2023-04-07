from django.urls import re_path, path
from . import views

urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('registration/logout', views.logout_page, name='logout'),
]
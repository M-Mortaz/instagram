from django.urls import path, re_path

from . import views

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
]

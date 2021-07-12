from django.urls import path, include

from .api import views

app_name = 'social'

urlpatterns = [
    path('api/', include('social.api.urls')),
]

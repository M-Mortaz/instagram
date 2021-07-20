from django.urls import path, re_path, include

app_name = 'user'

urlpatterns = [
    path('api/', include('user.api.urls', namespace='user-api')),
]

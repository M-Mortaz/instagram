from django.urls import path, include

app_name = 'location'

urlpatterns = [
    path('api/', include('location.api.urls', namespace='location-api')),
]

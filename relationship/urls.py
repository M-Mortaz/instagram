from django.urls import path, include

app_name = 'relationship'

urlpatterns = [
    path('api/', include('relationship.api.urls', namespace='relationship-api')),
]

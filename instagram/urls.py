from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/',
         include('user.urls', namespace='user')),

    path('social/',
         include('social.urls', namespace='social')),

    path('activity/',
         include('activity.urls', namespace='activity')),

    path('location/',
         include('location.urls', namespace='location')),

    path('relationship/',
         include('relationship.urls', namespace='relationship')),

    path('oauth/',
         include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('admin/',
         admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

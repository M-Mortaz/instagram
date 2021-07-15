from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/', include('user.urls')),
    path('social/', include('social.urls')),
    path('activity/', include('activity.urls')),
    path('location/',include('location.urls',namespace='location')),
    path('oauth/',
         include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from django.urls import path, re_path

from . import views

app_name = 'social-api'

urlpatterns = [
    path('get-update-delete/<slug:slug>/',
         views.PostRetrieveUpdateDestroy.as_view(), name='get-update-delete'),

    re_path(r'list-create/$',
            views.PostListCreate.as_view(), name='list-create'),

    path('list-create/<slug:slug>/',
         views.PostMediaView.as_view(), name='media-list-create'),
]

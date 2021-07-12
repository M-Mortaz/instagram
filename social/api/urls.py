from django.urls import path

from . import views

urlpatterns = [
    path('get-update-delete/<slug:slug>/', views.RetrieveUpdateDestroy.as_view(), name='get-update-delete'),
    path('list-create/', views.ListCreate.as_view(), name='list-create'),
    path('list-create/<slug:slug>/', views.MediaView.as_view(),name='media-list-create'),
]

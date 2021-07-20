from django.urls import path

from . import views

app_name = 'user-api'

urlpatterns = [
    path('list/',
         views.UserList.as_view(), name='user-list'),

    path('register/',
         views.UserRegister.as_view(), name='register'),

    path('update-delete-retrieve/<str:username>/',
         views.UserRetrieveDeleteUpdate.as_view(), name='retrieve-update-delete'),
]

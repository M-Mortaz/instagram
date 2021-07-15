from django.urls import path

from . import views

urlpatterns = [
    path('list/',
         views.UserList.as_view(), name='register'),

    path('register/',
         views.UserRegister.as_view(), name='register'),

    path('update-delete-retrieve/<str:username>/',
         views.UserRetrieveDeleteUpdate.as_view()),
]

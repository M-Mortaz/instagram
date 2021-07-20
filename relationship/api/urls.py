from django.urls import path

from . import views

app_name = 'relationship-api'

urlpatterns = [
    path('<str:username>/followers/',
         views.UserFollowers.as_view(), name='followers'),

    path('<str:username>/followers/requests/',
         views.FollowRequests.as_view(), name='requests'),

    path('<str:username>/followers/requests/<str:username2>/',
         views.UserFollowRequest.as_view(), name='user-request'),

    path('<str:username>/followings/',
         views.UserFollowings.as_view(), name='followings'),
]

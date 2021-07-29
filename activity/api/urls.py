from django.urls import path

from . import views

app_name = 'activity-api'

urlpatterns = [
    path('comment-list-create/<slug:slug>/',
         views.CommentListCreate.as_view(), name='comment-list-create'),

    path('comment-retrieve-update-delete/<slug:slug>/',
         views.CommentRetrieveUpdateDestroy.as_view(), name='comment-retrieve-update-delete'),

    path('comment-reply/<slug:slug>/',
         views.ReplyListCreate.as_view(), name='reply-list-create'),

    path('like-post-list-create/<slug:slug>/',
         views.PostLikeListCreate.as_view(), name='like-post-list-create'),

    path('like-comment-list-create/<slug:slug>/',
         views.CommentLikeListCreate.as_view(), name='like-comment-list-create'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('comment-list-create/<slug:slug>/',
         views.CommentListCreate.as_view(), name='comment-lc'),

    path('comment-retrieve-update-delete/<slug:slug>/',
         views.CommentRetrieveUpdateDestroy.as_view(), name='comment-rud'),

    path('comment-reply/<slug:slug>/',
         views.ReplyListCreate.as_view(), name='reply-create'),

    path('like-post-list-create/<slug:slug>/',
         views.PostLikeListCreate.as_view(), name='like-plc'),

    path('like-comment-list-create/<slug:slug>/',
         views.CommentLikeListCreate.as_view(), name='like-clc'),
]

from django.urls import path
from . import views

urlpatterns = [
    # path('create-cl/', views.CommentLikeCreate.as_view(), name='like-create'),
    path('comment-lc/<slug:slug>/', views.CommentListCreate.as_view(), name='comment-lc'),
    path('comment-rud/<slug:slug>/', views.CommentRetrieveUpdateDestroy.as_view(), name='comment-rud'),
    path('comment-reply/<slug:slug>/', views.ReplyListCreate.as_view(), name='reply-create'),
    path('like-plc/<slug:slug>/', views.PostLikeListCreate.as_view(), name='like-plc'),
]

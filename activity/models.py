from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from lib.shared_models import BaseModel
from social.models import Post

User = get_user_model()


class Comment(BaseModel):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    content  = models.TextField(_('content'))
    post     = models.ForeignKey(Post, on_delete=models.CASCADE)
    slug     = models.SlugField(_('Slug'), max_length=150, unique=True, default='')
    reply_to = models.ForeignKey('self', related_name='replies',
                            on_delete=models.CASCADE, null=True,
                            blank=True)

    def __str__(self):
        if self.reply_to is not None:
            return f'{self.user.username} ---> {self.reply_to.user.username}'
        return f'{self.user.username} ---> {self.post.slug}'

    class Meta:
        verbose_name        = _('Comment')
        verbose_name_plural = _('Comments')


class Like(BaseModel):
    user    = models.ForeignKey(User, related_name='likes',
                                      on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name        = _('Like')
        verbose_name_plural = _('Likes')


class LikeComment(BaseModel):
    like    = models.OneToOneField(Like, on_delete=models.CASCADE, related_name='like_comment')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name        = _('Like_comment')
        verbose_name_plural = _('Like_comments')

    def __str__(self):
        return f'{self.like.user.username} ---> {self.comment.slug}'


class LikePost(BaseModel):
    like = models.OneToOneField(Like, on_delete=models.CASCADE, related_name='like_post')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')


    class Meta:
        verbose_name        = _('Like_Post')
        verbose_name_plural = _('Like_Posts')

    def __str__(self):
        return f'{self.like.user.username} ---> {self.post.slug}'


class ViewMedia(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} ---> {self.post.slug}"

    class Meta:
        verbose_name        = _('View')
        verbose_name_plural = _('Views')

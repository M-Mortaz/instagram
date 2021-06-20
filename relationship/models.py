from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from lib.shared_models import BaseModel
from social.models import Post

User = get_user_model()


class BlackList(BaseModel):
    blocker = models.ForeignKey(User, related_name='blocked',
                                on_delete=models.CASCADE)
    blocked = models.ForeignKey(User, related_name='blocker',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blocker} ---> {self.blocked}"

    class Meta:
        verbose_name        = _('Blacklist')
        verbose_name_plural = _('Blacklists')


class Relation(BaseModel):
    from_user     = models.ForeignKey(User, related_name='followings',
                                 on_delete=models.CASCADE)
    to_user    = models.ForeignKey(User, related_name='followers',
                                 on_delete=models.CASCADE)
    confirmation = models.BooleanField(_('Confirmation'), default=False)

    def __str__(self):
        return f"{self.follower} ---> {self.following}"

    class Meta:
        verbose_name        = _('Relation')
        verbose_name_plural = _('Relations')


class Tag(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name        = _('Tag')
        verbose_name_plural = _('Tags')

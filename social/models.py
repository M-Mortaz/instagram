from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

from location.models import Location
from lib.shared_models import BaseModel
from lib.functions import rename_file

User = get_user_model()


class Post(BaseModel):
    user        = models.ForeignKey(User, related_name='posts',
                                 on_delete=models.CASCADE)
    caption     = models.TextField(_('Caption'), max_length=300, blank=True)
    location    = models.ForeignKey(Location, related_name='posts',
                                 on_delete=models.CASCADE)
    allow_share = models.BooleanField(default=True)
    slug        = models.SlugField(_('Slug'), max_length=150, unique=True)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name        = _('Post')
        verbose_name_plural = _('Posts')


class Media(BaseModel):
    post  = models.ForeignKey(Post,related_name='media', on_delete=models.CASCADE)
    media = models.FileField(upload_to=rename_file, blank=True, validators=[
                                 FileExtensionValidator(allowed_extensions=[
                                     'jpg', 'jpeg', 'png', 'mkv', 'mp4', 'flv'
                                 ])])

    class Meta:
        verbose_name        = _('media')
        verbose_name_plural = _('Media')

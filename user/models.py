from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

import re

from lib.functions import rename_profile
from location.models import Location
from lib.shared_models import BaseModel


class Business(models.Model):
    title        = models.CharField(_('title'), max_length=150, blank=True)
    location     = models.ManyToManyField(Location,related_name='business')
    email        = models.EmailField(_('email'), max_length=150, blank=True)
    phone_number = models.CharField(_('phone_number'), max_length=11, blank=True)
    preview_info = models.BooleanField(_('preview information'), default=False)

    def clean(self):
        super().clean()
        pat = r'^09\d{8}$'
        if not re.match(pat, str(self.phone_number)):
            raise ValidationError(
                {'phone_number': 'The correct format is 09*********'}
            )

    class Meta:
        verbose_name        = _('Business')
        verbose_name_plural = _('Business')

    def __str__(self):
        return self.title


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):

    username_validator = UnicodeUsernameValidator()
    user_help_text     = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    username           = models.CharField(_('username'),max_length=150, unique=True,
                                help_text=_(user_help_text),
                                validators=[username_validator], error_messages={
                                    'unique': _("A user with that username already exists."),
                                                                                },)

    first_name = models.CharField(_('first name'), max_length=40)
    last_name  = models.CharField(_('last name'), max_length=40)
    email      = models.EmailField(_('email address'),unique=True)
    is_staff   = models.BooleanField(_('staff status'),default=False,help_text=_(
                                    'Designates whether the user can log into this admin site.'),
                                    )
    is_active       = models.BooleanField(_('active'),default=True,help_text=_(
                                                'Determines whether user is active or not'),
                                         )
    date_joined     = models.DateTimeField(_('date joined'), default=timezone.now)
    objects         = UserManager()
    phone_number    = models.CharField(max_length=11, unique=True, blank=True, null=True)
    business        = models.OneToOneField(Business, blank=True, null=True,on_delete=models.CASCADE)
    is_verified     = models.BooleanField(default=False)
    avatar          = models.ImageField(upload_to=rename_profile, blank=True, null=True)
    bio             = models.TextField(blank=True)
    website_link    = models.URLField(max_length=150, blank=True)
    public_private  = models.BooleanField(default=False)

    EMAIL_FIELD     = 'email'
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name        = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
        pat = r'^09\d{9}$'
        if not re.match(pat, str(self.phone_number)):
            raise ValidationError(
                {'phone_number': 'The correct format is 09*********'}
            )

    def get_full_name(self):
        return str(self.first_name) + str(self.last_name)

    def get_short_name(self):
        return self.first_name

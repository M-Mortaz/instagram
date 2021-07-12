from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'user', 'slug'


@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = 'post',



from django.contrib import admin
from . import models


@admin.register(models.Like)
class AdminLike(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class AdminComment(admin.ModelAdmin):
    list_display = 'user', 'post', 'reply_to'


@admin.register(models.LikeComment)
class AdminLikeComment(admin.ModelAdmin):
    pass


@admin.register(models.LikePost)
class AdminLikePost(admin.ModelAdmin):
    pass


@admin.register(models.ViewMedia)
class AdminViewMedia(admin.ModelAdmin):
    pass

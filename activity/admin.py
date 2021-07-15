from django.contrib import admin
from . import models


@admin.register(models.Like)
class AdminLike(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class AdminComment(admin.ModelAdmin):
    list_display = 'user', 'post', 'reply_to_user','slug'

    def reply_to_user(self, obj):
        if obj.reply_to is not None:
            name = obj.reply_to.user.username
            return f'{obj.user.username} ---> {name}'
        return f'{obj.user.username} ---> {obj.post.slug}'

    reply_to_user.short_description = 'Reply To'


@admin.register(models.LikeComment)
class AdminLikeComment(admin.ModelAdmin):
    pass


@admin.register(models.LikePost)
class AdminLikePost(admin.ModelAdmin):
    pass


@admin.register(models.ViewMedia)
class AdminViewMedia(admin.ModelAdmin):
    pass

from django.contrib import admin
from . import models


@admin.register(models.Relation)
class RelationAdmin(admin.ModelAdmin):
    list_display = 'from_user', 'to_user', 'confirmation', 'created'

    def from_user(self, obj):
        return obj.from_user.user.username

    def to_user(self, obj):
        return obj.to_user.user.username


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'user', 'post'


@admin.register(models.BlackList)
class BlackListAdmin(admin.ModelAdmin):
    list_display = 'blocker', 'blocked'

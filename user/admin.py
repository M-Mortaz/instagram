from django.contrib import admin
from django.contrib.auth.hashers import make_password

from . import models

admin.site.register(models.Business)


@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal', {
            'fields': (
                'username', 'password', 'first_name', 'last_name',
                'phone_number', 'avatar', 'email', 'bio', 'type_business')
        }),
        ('Security', {
            'fields': ('is_verified', 'is_staff', 'public_private'),
        }),
    )
    list_display = ('username', 'first_name', 'last_name', 'email')

    def save_model(self, request, obj, form, change):
        password     = form.cleaned_data['password']
        obj.password = make_password(password)
        obj.save()

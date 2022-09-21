from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Card, Style, Comment, Follow

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Card)
admin.site.register(Style)
admin.site.register(Comment)
admin.site.register(Follow)
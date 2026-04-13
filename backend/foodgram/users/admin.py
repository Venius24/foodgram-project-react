from django.contrib import admin
from .models import User, Follow  # Заменили Subscription на Follow

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_moderator')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    list_editable = ('is_moderator',)

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    search_fields = ('user__username', 'following__username')
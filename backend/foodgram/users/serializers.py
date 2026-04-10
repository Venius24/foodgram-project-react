from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(UserSerializer):
    # Фронтенд Foodgram часто просит проверку подписки (is_subscribed)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        # Если пока нет системы подписок, просто возвращаем False
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        # Здесь будет логика проверки подписки
        return False

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'password')
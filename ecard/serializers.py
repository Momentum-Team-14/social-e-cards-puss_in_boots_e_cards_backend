from rest_framework import serializers
from .models import Card, CustomUser, Style, Comment, Follow

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username')


class CommentSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer()
    class Meta:
        model = Comment
        fields = ('pk', 'owner', 'card', 'text')


class CardSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)

    class Meta:
        model = Card
        fields = ("pk", "owner", "title", "outer_message", "inner_message")

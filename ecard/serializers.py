from dataclasses import fields
from rest_framework import serializers
from .models import Card, CustomUser, Style, Comment, Follow
from django.db import IntegrityError

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('pk', 'username')


class StyleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Style
        fields = ('pk', 'card_color', 'border', 'border_color', 'font', 'font_color', 'text_align')


class CommentSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('pk', 'owner', 'card', 'text')


class CardSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    style = StyleSerializer(read_only=True)
    
    class Meta:
        model = Card
        fields = ('pk', 'owner', 'title', 'outer_message', 'inner_message', 'style', 'comments')


class CardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('title', 'outer_message', 'inner_message', 'style')


class FollowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Follow
        fields = ('pk', 'followee')
        
from dataclasses import fields
from rest_framework import serializers
from .models import Card, CustomUser, Style, Comment, Follow


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'username')


class StyleSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ('card_color', 'border', 'border_color', 'font', 'font_color', 'text_align')


class CommentSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('pk', 'owner', 'card', 'text')


class CardSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    style = StyleSerialzier(read_only=True)
    class Meta:
        model = Card
        fields = ('pk', 'owner', 'title', 'outer_message', 'inner_message', 'style', 'comments')


class FollowSerializer(serializers.ModelSerializer):
    follower = CustomUserSerializer(read_only=True)
    followee = CustomUserSerializer(read_only=True)
    class Meta:
        model = Follow
        fields = ('pk', 'follower', 'followee')
        
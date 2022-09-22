from rest_framework import serializers
from .models import Card, Style, Comment, Follow

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('pk', 'owner', 'title', 'outer_message', 'inner_message','style')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('pk', 'owner', 'card', 'text')
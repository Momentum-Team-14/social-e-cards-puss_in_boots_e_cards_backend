from rest_framework import serializers
from .models import Card, Style, Comment, Follow

class CardSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model = Card
        fields = ('pk', 'owner', 'title', 'outer_message', 'inner_message','style')

    def get_owner(self, obj):
        name = obj.owner.username
        pk = obj.owner.pk
        return pk, name


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('pk', 'owner', 'card', 'text')

    def get_owner(self, obj):
        name = obj.owner.username
        pk = obj.owner.pk
        return pk, name
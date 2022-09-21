from rest_framework import serializers
from .models import Card, Style, Comment, Follow

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('owner', 'title', 'outer_message', 'inner_message','style', )


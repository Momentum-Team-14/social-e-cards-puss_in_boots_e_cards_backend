from rest_framework import generics
from .models import Card, Comment, Style, Follow
from .serializers import CardSerializer, CommentSerializer, StyleSerialzier, FollowSerializer
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserCardList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = Card.objects.filter(owner=self.request.user.pk)
        return queryset


class UserCommentList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(owner=self.request.owner.pk)
        return queryset


class StyleCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Style.objects.all()
    serializer_class = StyleSerialzier


class FollowList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def get_queryset(self):
        queryset = Follow.objects.filter(follower=self.request.user.pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class RemoveFollow(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

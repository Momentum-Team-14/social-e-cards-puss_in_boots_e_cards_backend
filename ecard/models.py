from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Card(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'cards')
    title = models.CharField(max_length=300)
    outer_message = models.TextField()
    inner_message = models.TextField()
    style = models.ForeignKey('Style',on_delete=models.CASCADE, related_name = 'cards')

    def __str__(self):
        return f'{self.title} by: {self.owner}'

class Style(models.Model):
    style = models.CharField (max_length=300)

    def __str__(self):
        return f'{self.style}'


class Comment(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'comments')
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name = 'comments')
    text = models.TextField()

    def __str__(self):
        return f'{self.text} by:{self.owner} on {self.card}'

class Follow(models.Model):
    follower = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'following')
    followee = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'followers')

    def __str__(self):
        return f'{self.follower} following {self.followee}'





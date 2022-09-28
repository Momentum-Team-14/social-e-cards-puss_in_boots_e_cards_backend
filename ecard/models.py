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
    CARD_COLOR_CHOICES = (
        ('white', 'WHITE'),
        ('red','RED'),
        ('yellow', 'YELLOW'),
        ('green','GREEN'),
        ('blue', 'BLUE'),
        ('black','BLACK'),
        ('pink', 'PINK'),
        ('purple', 'PURPLE'),
        ('orange','ORANGE'),
    )
    
    BORDER_CHOICES = (
        ('solid', 'SOLID'),
        ('dotted', 'DOTTED'),
        ('ridge', 'RIDGE'),
        ('double', 'DOUBLE'),
        ('groove', 'GROOVE'),
    )
    
    BORDER_COLOR_CHOICES = (
        ('white', 'WHITE'),
        ('red','RED'),
        ('yellow', 'YELLOW'),
        ('green','GREEN'),
        ('blue', 'BLUE'),
        ('black','BLACK'),
        ('pink', 'PINK'),
        ('purple', 'PURPLE'),
        ('orange','ORANGE'),
    )

    FONT_CHOICES = (
        ('lobster', 'LOBSTER'),
        ('papyrus', 'PAPYRUS'),
        ('comic_sans', 'COMIC_SANS'),
    )

    FONT_COLOR_CHOICES = (
        ('white', 'WHITE'),
        ('red','RED'),
        ('yellow', 'YELLOW'),
        ('green','GREEN'),
        ('blue', 'BLUE'),
        ('black','BLACK'),
        ('pink', 'PINK'),
        ('purple', 'PURPLE'),
        ('orange','ORANGE'),
    )

    TEXT_ALIGN_CHOICES = (
        ('left', 'LEFT'),
        ('center', 'CENTER'),
        ('right', 'RIGHT'),
    )
    
    card_color = models.CharField(max_length=6, choices=CARD_COLOR_CHOICES, default='white')
    border = models.CharField(max_length=6, choices=BORDER_CHOICES, default='solid')
    border_color = models.CharField(max_length=6, choices=BORDER_COLOR_CHOICES, default='white')
    font = models.CharField(max_length=10, choices=FONT_CHOICES, default='lobster')
    font_color = models.CharField(max_length=6, choices=FONT_COLOR_CHOICES, default='black')
    text_align = models.CharField(max_length=6, choices=TEXT_ALIGN_CHOICES, default='left')

    def __str__(self):
        return f'Card options selected: card color: {self.card_color}, border: {self.border}, border color: {self.border_color}, font: {self.font}, font color: {self.font_color}, alignment: {self.text_align}'


class Comment(models.Model):
    owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'comments')
    card = models.ForeignKey(Card,on_delete=models.CASCADE, related_name = 'comments')
    text = models.TextField()

    def __str__(self):
        return f'{self.text} by:{self.owner} on {self.card}'


class Follow(models.Model):
    follower = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name = 'following')
    followee = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name = 'followers')

    def __str__(self):
        return f'{self.follower} following {self.followee}'





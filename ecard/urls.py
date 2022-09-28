from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ecard import views

urlpatterns = [
<<<<<<< HEAD
    path('ecard/', views.CardList.as_view()),
    path('ecard/<int:pk>/', views.CardDetail.as_view()),
    path('ecard/user/', views.UserCardList.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('comments/user/', views.CommentDetail.as_view()),
    path('styles/', views.StyleCreate.as_view()),
    path('following/', views.FollowList.as_view()),
    path('following/delete/<int:pk>/', views.RemoveFollow.as_view()),
=======
    path('', views.api_root),
    path('ecard/', views.CardList.as_view(), name='ecard_list'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('ecard/user/', views.UserCardList.as_view(), name='user_ecards'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('comments/user/', views.CommentDetail.as_view(), name='user_comments'),
    path('styles/', views.StyleCreate.as_view(), name='styles'),
>>>>>>> main
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ecard import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/', views.CardList.as_view(), name='ecard_list'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('ecard/user/<int:pk>', views.UserCardList.as_view(), name='user_ecards'),
    path('comments/', views.CommentList.as_view(), name='comment_list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('comments/user/', views.CommentDetail.as_view(), name='user_comments'),
    path('styles/', views.StyleCreate.as_view(), name='styles'),
    path('following/', views.FollowList.as_view(), name='following_list'),
    path('following/<int:pk>/', views.FollowDetail.as_view(), name='follow_detail'),
    path('users/', views.UserList.as_view, name='all_users' )
]

urlpatterns = format_suffix_patterns(urlpatterns)
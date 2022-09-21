from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from ecard import views

urlpatterns = [
    path('ecard/', views.CardList.as_view()),
    path('ecard/<int:pk>/', views.CardDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
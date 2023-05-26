from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsStartPage.as_view(), name='home'),
    path('<int:pk>/', NewsDetailCommentFormView.as_view(), name='news_detail'),
    path('add_news/', NewsFormView.as_view()),
    path('<int:pk>/edit/', NewsEditFormView.as_view())
]

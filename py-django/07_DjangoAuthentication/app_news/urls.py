from unicodedata import name
from django.urls import path
from .views import *
from app_users.views import LoginView, LogoutView

urlpatterns = [
    path('', NewsStartPage.as_view(), name='home'),
    path('<int:pk>/', NewsDetailCommentFormView.as_view(), name='news_detail'),
    path('add_news/', NewsAdd.as_view()),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='edit'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

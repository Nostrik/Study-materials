from django.urls import path
from .views import *


urlpatterns = [
    path('', AdvertisementListView.as_view()),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view()),
    path('profiles/register/', UserFormView.as_view()),
    path('profiles/<int:profile_id>/edit/', UserEditFormView.as_view())
]

from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view()),
    path('categories/', views.categories),
    path('regions/', views.Regions.as_view()),
    path('advertisement/', views.AdvertisementListView.as_view()),
    path('', views.AdvertisementListView.as_view()),
    # path('advertisement/list/', views.advertisement_list)
]

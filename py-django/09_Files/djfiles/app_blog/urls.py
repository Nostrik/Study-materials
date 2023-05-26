from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogStartView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', another_register_view, name='register'),
    path('user_info/', show_user_info, name='user_info'),
    path('user_edit/', user_edit_info, name='user_edit'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('add_entry/', EntryAdd.as_view(), name='entry_add'),
    path('add_from_file/', add_entry_from_csv, name='add_from_file')
]

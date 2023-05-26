from django.urls import path
from .import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path('advertisement/', views.advertisement_detail, name='advertisement_list'),
    path("course_1/", views.first_course, name='advertisement_list'),
    path("course_2/", views.second_course, name='advertisement_list'),
    path("course_3/", views.third_course, name='advertisement_list'),
    path("course_4/", views.fourth_course, name='advertisement_list'),
    path("course_5/", views.fifth_course, name='advertisement_list')
    # path("<course_name>", views.show_courses, name='advertisement_list'),
]

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})
    # return HttpResponse('<p>Hello</p>')


def advertisement_detail(request, *args, **kwargs):
    return HttpResponse('<ul>'
                        '<li>advertisement_detail</li>'
                        '<li>advertisement_detail</li>'
                        '<li>advertisement_detail</li>'
                        '</ul>'
                        )


def first_course(request, *args, **kwargs):
    return render(request, 'advertisement/course_1.html', {})


def second_course(request, *args, **kwargs):
    return render(request, 'advertisement/course_2.html', {})


def third_course(request, *args, **kwargs):
    return render(request, 'advertisement/course_3.html', {})


def fourth_course(request, *args, **kwargs):
    return render(request, 'advertisement/course_4.html', {})


def fifth_course(request, *args, **kwargs):
    return render(request, 'advertisement/course_5.html', {})


# def show_courses(request, course_name, *args, **kwargs):
#     if course_name == 'course_1/':
#         return render(request, 'advertisement/course_1.html', {})
#     else:
#         return HttpResponseNotFound()


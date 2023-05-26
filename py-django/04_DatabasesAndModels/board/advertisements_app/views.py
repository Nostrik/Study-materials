from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Advertisement


# class Advertisement_start(TemplateView):
#     template_name = 'advertisement/advertisement_list.html'


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advertisement/advertisement_list.html'
    context_object_name = 'advertisements_list'
    queryset = Advertisement.objects.all()
    extra_context = {'title': 'Главная страница'}

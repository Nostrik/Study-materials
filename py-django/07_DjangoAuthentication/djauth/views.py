from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, 'app_news_list.html')
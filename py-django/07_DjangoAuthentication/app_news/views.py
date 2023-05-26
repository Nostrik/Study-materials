import pprint
from this import s
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def show_me(obj):
    print('#' * 80)
    # pprint.pprint(obj)
    print(obj)
    print('#' * 80)


class NewsStartPage(ListView):
    model = News
    template_name = 'app_news/app_news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.order_by('created_at')


class NewsDetail(DetailView):
    model = News
    template_name = 'app_news/app_news_detail.html'


class CommentFormView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments_list = self.object.comments.all()
        context['comment_list'] = comments_list
        context['comment_form'] = CommentForm()
        return context


class NewsDetailCommentFormView(DetailView):
    model = News
    template_name = 'app_news/app_news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = self.object.comments.all()
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context

    def post(self, request, pk):
        user_name = request.user
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            news_instance = self.get_object()
            new_comment.news = news_instance

            if request.user.is_authenticated:
                new_comment.user_name = user_name
            else:
                a = request.POST['user_name']  # user_name this not authenticated
                new_comment.user_name = str(a + '  аноним')

            new_comment.save()
        else:
            comment_form.add_error('__all__', 'Ошибка ввода')

        return HttpResponseRedirect('/')


class NewsFormView(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/add_news.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'app_news/add_news.html', context={'news_form': news_form})


class NewsEditFormView(View):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/news_edit.html', context={'news_form': news_form, 'news_id': pk})

    def post(self, request, pk):
        news = News.objects.get(id=pk)
        news_form = NewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news.save()
        return render(request, 'app_news/news_edit.html', context={'news_form': news_form, 'news_id': pk})


class NewsAdd(CreateView):
    model = News
    fields = ['title', 'description', 'actual']
    template_name = 'app_news/add_news.html'
    success_url = reverse_lazy('home')


class NewsUpdate(UpdateView):
    model = News
    fields = ['title', 'description', 'actual']
    template_name = 'app_news/news_edit.html'
    success_url = reverse_lazy('home')

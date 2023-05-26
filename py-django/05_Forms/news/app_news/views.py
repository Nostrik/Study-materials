from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import News, Comment
from .forms import *
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse


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
        comment_form = CommentForm(request.POST)
        new_comment = comment_form.save(commit=False)
        news_instance = self.get_object()
        new_comment.news = news_instance
        new_comment.save()
        # return redirect('/')


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


import pprint
from this import s
from django.core.exceptions import PermissionDenied
from urllib import request
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import *
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


def show_me(obj):
    print('#' * 80)
    # pprint.pprint(obj)
    print(obj)
    print('#' * 80)


class NewsStartPage(ListView):
    model = News
    template_name = 'app_news/app_news_list.html'
    context_object_name = 'news_list'
    param = ''

    def get_queryset(self):
        qs = super().get_queryset()
        param = ''
        try:
            param = self.request.GET['tag']
        except:
            pass
        return qs.filter(description__icontains=param)


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


class NewsAdd(PermissionRequiredMixin, CreateView):
    model = News
    permission_required = 'app_news.add_news'
    fields = ['title', 'description', 'actual']
    template_name = 'app_news/add_news.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if self.request.user.has_perm('app_news.can_publish'):
            return super().form_valid(form)
        else:
            raise PermissionDenied


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    model = News
    permission_required = 'app_news.change_news'
    fields = ['title', 'description', 'actual']
    template_name = 'app_news/news_edit.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if self.request.user.has_perm('app_news.can_publish'):
            return super().form_valid(form)
        else:
            raise PermissionDenied


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'app_news/register.html', {'form': form})


def expanded_register_view(request):
    if request.method == 'POST':
        form = ExpandedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            telephone = form.cleaned_data.get('telephone')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                telephone=telephone,
                city=city
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExpandedRegisterForm()
    return render(request, 'app_news/register.html', {'form': form})


def show_user_info(request):
    user_info = request.user
    return render(request, 'app_news/user_info.html', {'user': user_info})

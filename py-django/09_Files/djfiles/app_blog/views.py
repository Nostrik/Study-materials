from _csv import reader

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Entry, Picture, Profile, UploadFileUpd
from .forms import *


def show_me(obj):
    print('#' * 80)
    # pprint.pprint(obj)
    print(obj)
    print('#' * 80)


class BlogStartView(ListView):
    model = Entry
    template_name = 'note_list.html'


class BlogDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'
    # queryset = Picture.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        files = self.object.picture_set.all()
        files_ready = []
        for kek in files:
            files_ready.append(kek.file)
        context['files_list'] = files_ready
        return context


class LoginView(LoginView):
    template_name = 'login.html'


class LogoutView(LogoutView):
    next_page = '/blog/'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blog/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterFormExp(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            Profile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blog/')
    else:
        form = RegisterFormExp()
    return render(request, 'register.html', {'form': form})


def show_user_info(request):
    user_info = request.user
    return render(request, 'user_info.html', {'user': user_info})


def user_edit_info(request):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/blog/')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'user_edit_info.html', {'form': profile_form})


def add_entry_from_csv(request):
    if request.method == 'POST':
        upload_file_form = UploadEntryForm(request.POST, request.FILES)
        # upload_file = UploadFileUpd(request.POST, request.FILES)
        if upload_file_form.is_valid():
            entry_file = upload_file_form.cleaned_data['file'].read()
            entry_str = entry_file.decode('utf-8').split('\n')
            csv_reader = reader(entry_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                try:
                    data = Entry(title=row[0], text=row[1])
                    data.save()
                except:
                    pass
            return redirect('/blog/')
    else:
        upload_file_form = UploadEntryForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'add_entry_from_file.html', context=context)


class EditUserInfo(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name']
    template_name = 'user_edit.html'


class EntryAdd(PermissionRequiredMixin, CreateView):
    model = Entry
    permission_required = 'app_blog.add_entry'
    fields = ['title', 'text']
    template_name = 'add_entry.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = MultiFileForm()
        return context

    def post(self, request, *args, **kwargs):
        post = super().post(request, *args, **kwargs)
        files_form = MultiFileForm(request.POST, request.FILES)
        if files_form.is_valid():
            files = request.FILES.getlist('file_field')
            show_me(len(files))
            entry_instance = self.object
            for f in files:
                instance = Picture(file=f, entry=entry_instance)
                instance.save()
        return post

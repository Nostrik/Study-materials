from django import forms
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user_name', 'text']


class ExpandedRegisterForm(UserCreationForm):
    telephone = forms.CharField(max_length=15, required=False, help_text='Телефон')
    city = forms.CharField(max_length=36, required=False, help_text='Город')
    # verify = forms.BooleanField()
    # news_quantity = forms.CharField(max_length=4, required=False)

    class Meta:
        model = User
        fields = ('username', 'last_name', 'password1', 'password2')
        help_texts = {
            'username': None
        }

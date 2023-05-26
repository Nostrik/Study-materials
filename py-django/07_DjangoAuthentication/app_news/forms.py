from django import forms
from.models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user_name', 'text']

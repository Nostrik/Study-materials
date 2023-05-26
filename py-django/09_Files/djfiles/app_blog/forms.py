from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Entry, Picture, Profile


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class MultiFileModelForm(forms.ModelForm):
    # file_filed = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Picture
        fields = ['file']


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class RegisterFormExp(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password': 'Пароль'
        }


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')


class UploadEntryForm(forms.Form):
    file = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ()
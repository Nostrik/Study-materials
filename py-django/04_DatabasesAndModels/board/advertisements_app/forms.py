from django import forms
import datetime
from django.core.exceptions import ValidationError
from .models import User


class UserForm(forms.ModelForm):
    # username = forms.CharField()
    # password = forms.CharField()
    # first_name = forms.CharField()
    # second_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # birthday = forms.DateField()

    # def clean_birthday(self):
    #     data = self.cleaned_data['birthday']
    #     today = datetime.date.today()
    #     year_delta = (today - data).days / 365
    #     if year_delta < 18:
    #         raise ValidationError('Только лица старше 18ти лет')
    #     return data
    #
    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')
    #     if first_name == 'Иван' and last_name == 'Иванов':
    #         msg = 'Иван Иванов запрещено'
    #         self.add_error('first_name', msg)
    #         self.add_error('last_name', msg)
    class Meta:
        model = User
        fields = '__all__'


class AdvertisementForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.CharField()

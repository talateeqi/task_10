from django import forms
from .models import Restaurant
from django.contrib.auth.models import User
from .models import Item

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'opening_time', 'closing_time', 'logo']

        widgets = {
        	'opening_time': forms.TimeInput(attrs={'type':'time'}),
        	'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ['name', 'description', 'price']

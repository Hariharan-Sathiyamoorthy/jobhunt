from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class userLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "username"}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "Password"}), required=True)

    class Meta:
        model = User
        fields = ['username', 'password']

class userRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "username"}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control',"placeholder": "Email"}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "Password"}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder": "Confirm Password"}), required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


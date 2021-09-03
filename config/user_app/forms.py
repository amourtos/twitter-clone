from django import forms
from user_app.models import TwitterUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = TwitterUser
        fields = ['username', 'password', 'email']

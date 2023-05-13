from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TeacherCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'New Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    experties = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Experties'}))
    join_date = forms.DateField(required=True, label="", widget=forms.DateInput(
        attrs={'placeholder': 'Date of Birth', 'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'join_date', 'experties', 'password1', 'password2']

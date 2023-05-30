from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TeacherCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={}))
    experties = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={}))
    join_date = forms.DateField(required=True, label="", widget=forms.DateInput(
        attrs={'class':'textbox-n', 'type': 'text','onfocus':"(this.type='date')"}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'join_date', 'experties', 'password1', 'password2']

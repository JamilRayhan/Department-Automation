from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from Login_App.models import UserProfile
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.crypto import get_random_string


class CreateNewUser(UserCreationForm):
    name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'New Password'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))

    # custom fields
    student_id = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder': 'Student ID'}))
    date_of_birth = forms.DateField(required=True, label="Date Of Birth", widget=forms.DateInput(
        attrs={'placeholder': 'Date of Birth', 'type': 'date'}))
    hall_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Hall Name'}))
    exam_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Exam Name'}))
    department_name = forms.CharField(required=True, label="", max_length=300, widget=forms.TextInput(
        attrs={'placeholder': 'Department Name'}))
    academic_year = forms.CharField(required=True, label="", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Academic Year'}))
    father_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(
        attrs={'placeholder': "Father's Name"}))
    mother_name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(
        attrs={'placeholder': "Mother's Name"}))
    permanent_address = forms.CharField(required=True, label="", max_length=300, widget=forms.TextInput(
        attrs={'placeholder': 'Permanent Address'}))
    nationality = forms.CharField(required=True, label="", max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Nationality'}))

    class Meta:
        model = User
        fields = ('name', 'email', 'username', 'password1', 'password2', 'student_id', 'date_of_birth', 'hall_name',
                  'exam_name', 'department_name', 'academic_year', 'father_name', 'mother_name', 'permanent_address', 'nationality')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already in use.")
        return email

    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if UserProfile.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError(
                "This student ID is already registered.")
        return student_id

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            user_profile = UserProfile.objects.create(user=user)
            user_profile.full_name = self.cleaned_data.get('name')
            user_profile.student_id = self.cleaned_data.get('student_id')
            user_profile.dob = self.cleaned_data.get('date_of_birth')
            user_profile.hall_name = self.cleaned_data.get('hall_name')
            user_profile.exam_name = self.cleaned_data.get('exam_name')
            user_profile.department_name = self.cleaned_data.get(
                'department_name')
            user_profile.academic_year = self.cleaned_data.get('academic_year')
            user_profile.father_name = self.cleaned_data.get('father_name')
            user_profile.mother_name = self.cleaned_data.get('mother_name')
            user_profile.permanent_address = self.cleaned_data.get(
                'permanent_address')
            user_profile.nationality = self.cleaned_data.get('nationality')
            user_profile.save()
        return user


class AuthForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        required=True,
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        exclude = ('user',)

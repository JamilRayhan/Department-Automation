from django import forms


class ExamRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # Add more fields for the exam registration form

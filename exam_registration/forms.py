from django import forms


class ExamRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=10)
    year = forms.CharField(max_length=10)
    semister = forms.CharField(max_length=10)
    hall_name = forms.CharField(max_length=100)
    exam_name = forms.CharField(max_length=100)
    department_name = forms.CharField(max_length=100)
    academic_year = forms.CharField(max_length=20)
    exam_hall = forms.CharField(max_length=100)
    father_name = forms.CharField(max_length=100)
    mother_name = forms.CharField(max_length=100)
    present_address = forms.CharField(max_length=100)
    permanent_address = forms.CharField(max_length=100)
    nationality = forms.CharField(max_length=50)
    date_of_birth = forms.DateField()
    # Add more fields for the exam registration form

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from .forms import TeacherCreationForm
from Login_App.models import Student
from Login_App.forms import StudentForm
from django.forms import formset_factory
# Define a user test function to check if user is an admin


def is_admin(user):
    return user.is_superuser

# Only allow admin to access this view


@login_required
@user_passes_test(is_admin)
def create_teacher(request):
    if request.method == 'POST':
        teacher_form = TeacherCreationForm(request.POST)
        if teacher_form.is_valid():
            user = teacher_form.save(commit=False)
            user.is_staff = True
            user.save()
            messages.success(request, 'Teacher account created successfully!')
    else:
        # changed from form = TeacherCreationForm()
        teacher_form = TeacherCreationForm()
    return render(request, 'adminpanel/create_teacher.html', context={'title': 'Create Teacher Account', 'teacher_form': teacher_form})


StudentFormSet = formset_factory(StudentForm, extra=1)


@login_required
@user_passes_test(is_admin)
def add_student(request):
    if request.method == 'POST':
        formset = StudentFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                student_id = form.cleaned_data.get('student_id')
                name = form.cleaned_data.get('name')
                date_of_birth = form.cleaned_data.get('date_of_birth')
                session = form.cleaned_data.get('session')
                hall = form.cleaned_data.get('hall')
                blood_group = form.cleaned_data.get('blood_group')
                permanent_address = form.cleaned_data.get('permanent_address')

                # Create a new student object
                student = Student(
                    student_id=student_id,
                    name=name,
                    date_of_birth=date_of_birth,
                    session=session,
                    hall=hall,
                    blood_group=blood_group,
                    permanent_address=permanent_address
                )
                student.save()

            # Redirect to a success page or perform any other desired action
            return HttpResponseRedirect(reverse('adminpanel:add_student'))
    else:
        formset = StudentFormSet()

    return render(request, 'adminpanel/add_student.html', {'formset': formset})

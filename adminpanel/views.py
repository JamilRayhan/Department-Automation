from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import TeacherCreationForm

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

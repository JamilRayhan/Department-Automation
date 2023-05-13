from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from .forms import ExamRegistrationForm
from Login_App.forms import CreateNewUser
from Login_App.models import UserProfile
from reportlab.pdfgen import canvas


@login_required
@user_passes_test(lambda u: not u.is_staff)
def exam_registration(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    initial_data = {
        'name': user_profile.full_name,
        'student_id': user_profile.student_id,
        'date_of_birth': user_profile.dob,
        'hall_name': user_profile.hall_name,
        'exam_name': user_profile.exam_name,
        'department_name': user_profile.department_name,
        'academic_year': user_profile.academic_year,
        'father_name': user_profile.father_name,
        'mother_name': user_profile.mother_name,
        'permanent_address': user_profile.permanent_address,
        'present_address': user_profile.present_address,
        'nationality': user_profile.nationality,
    }
    if request.method == 'POST':
        reg_form = ExamRegistrationForm(request.POST, initial=initial_data)
        if reg_form.is_valid():
            # Handle form submission
            # ...

            # Generate PDF
            template = get_template(
                'exam_registration/exam_registration_pdf.html')
            context = {'reg_form': reg_form}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="exam_registration.pdf"'
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 750, "Exam Registration Form")
            p.drawString(100, 700, f"Name: {reg_form.cleaned_data['name']}")
            p.drawString(
                100, 650, f"Student ID: {reg_form.cleaned_data['student_id']}")
            p.drawString(100, 600, f"Year: {reg_form.cleaned_data['year']}")
            p.drawString(
                100, 550, f"Semester: {reg_form.cleaned_data['semister']}")
            p.drawString(
                100, 500, f"Hall Name: {reg_form.cleaned_data['hall_name']}")
            p.drawString(
                100, 450, f"Exam Name: {reg_form.cleaned_data['exam_name']}")
            p.drawString(
                100, 400, f"Department Name: {reg_form.cleaned_data['department_name']}")
            p.drawString(
                100, 350, f"Academic Year: {reg_form.cleaned_data['academic_year']}")
            p.drawString(
                100, 300, f"Exam Hall: {reg_form.cleaned_data['exam_hall']}")
            p.drawString(
                100, 250, f"Father Name: {reg_form.cleaned_data['father_name']}")
            p.drawString(
                100, 200, f"Mother Name: {reg_form.cleaned_data['mother_name']}")
            p.drawString(
                100, 150, f"Present Address: {reg_form.cleaned_data['present_address']}")
            p.drawString(
                100, 100, f"Permanent Address: {reg_form.cleaned_data['permanent_address']}")
            p.drawString(
                100, 50, f"Nationality: {reg_form.cleaned_data['nationality']}")
            p.drawString(
                100, 20, f"Date of Birth: {reg_form.cleaned_data['date_of_birth']}")
            p.showPage()
            p.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response
    else:
        reg_form = ExamRegistrationForm(initial=initial_data)
    return render(request, 'exam_registration/exam_registration.html', {'reg_form': reg_form})


@login_required
def exam_registration_success(request):
    return render(request, 'exam_registration/exam_registration_success.html')

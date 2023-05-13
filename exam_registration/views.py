from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from .forms import ExamRegistrationForm
from reportlab.pdfgen import canvas

@login_required
@user_passes_test(lambda u: not u.is_staff)
def exam_registration(request):
    user = request.user
    initial_data = {
        'name': user.get_full_name(),
        'email': user.email,
    }
    if request.method == 'POST':
        reg_form = ExamRegistrationForm(request.POST, initial=initial_data)
        if reg_form.is_valid():
            # Handle form submission
            # ...

            # Generate PDF
            template = get_template('exam_registration/exam_registration_pdf.html')
            context = {'reg_form': reg_form}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="exam_registration.pdf"'
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 750, "Exam Registration Form")
            p.drawString(100, 700, f"Name: {reg_form.cleaned_data['name']}")
            # add other fields as necessary
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

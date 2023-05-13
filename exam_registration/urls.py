from django.urls import path
from . import views

urlpatterns = [
    path('register-for-exam/', views.exam_registration, name='exam_registration'),
    path('registration-success/', views.exam_registration_success, name='exam_registration_success'),
]

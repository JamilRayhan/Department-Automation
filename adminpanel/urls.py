from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('create-teacher/', views.create_teacher, name='create_teacher'),
    path('add-student/', views.add_student, name='add_student'),
]
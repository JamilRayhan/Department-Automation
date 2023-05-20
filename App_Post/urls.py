from App_Post import views
from django.urls import path
app_name= 'App_Post'

urlpatterns = [
    path('', views.home,name='home'),
    path('questions/',views.questions,name='questions'),
    path('add_ans/<int:post_id>/', views.add_ans, name='add_ans'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
]

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    student_id = models.CharField(max_length=10, blank=True, null=True)
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    hall_name = models.CharField(max_length=100, blank=True)
    exam_name = models.CharField(max_length=100, blank=True)
    department_name = models.CharField(max_length=300, blank=True)
    academic_year = models.CharField(max_length=20, blank=True)
    father_name = models.CharField(max_length=100, blank=True)
    mother_name = models.CharField(max_length=100, blank=True)
    permanent_address = models.CharField(max_length=300, blank=True)
    present_address = models.CharField(max_length=300, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    session = models.CharField(max_length=50)
    hall = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=10)
    permanent_address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
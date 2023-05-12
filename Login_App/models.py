from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    description = models.TextField(blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    dob = models.DateField(blank=True, null=True)
    student_id = models.CharField(max_length=10, blank=True, null=True)  # Add the student_id field
    website = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from Login_App.models import UserProfile,Follow
from django.contrib.auth.models import User
from App_Post.models import Posts
# Create your views here.


@login_required
def home(request):
    user=request.user
    if request.method == 'GET':
        search = request.GET.get('search',  ' ')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_Post/home.html', context={'title': 'Home', 'search': search, 'result': result,'user':user})

@login_required
def questions(request):
    following_list= Follow.objects.filter(follower=request.user)
    posts= Posts.objects.filter(author__in=following_list.values_list('following'))
    return render(request, 'App_Post/questions.html', context={'title': 'Frequently Asked Question','posts':posts})
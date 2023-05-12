from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Login_App.forms import CreateNewUser,AuthForm,EditProfile
from Login_App.models import UserProfile,Follow
from App_Post.forms import PostForm
from django.contrib.auth.models import User
#from App_Post.forms import PostForm
# Create your views here.


def sign_up(request):
    form= CreateNewUser()
    registered= False
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile= UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('Login_App:login'))
    dict= {'title':'Sign up','form':form,'registered':registered}
    return render(request,'Login_App/signup.html',context=dict)

def login_page(request):
    form=AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Post:home'))
    return render(request, 'Login_App/login.html',context={'title':'Login','form':form} )


@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form= EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form=EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request,'Login_App/profile.html',context={'form':form,'title':'Edit Profile . Social'})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:login'))


@login_required
def profile(request):
    post_form = PostForm()
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Login_App/user.html', context={'title':request.user.username, 'post':post_form})


@login_required
def user(request,username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user,following= user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('Login_App:profile'))
    return render(request,'Login_App/user_other.html',context={'user_other':user_other,'already_followed':already_followed})

@login_required
def follow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user,following= following_user)
    
    if not already_followed:
        followed_user=Follow(follower=follower_user,following= following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('Login_App:user', kwargs={'username':username}))

@login_required
def unfollow(request,username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user,following= following_user)
    already_followed.delete()
    
    return HttpResponseRedirect(reverse('Login_App:user', kwargs={'username':username}))


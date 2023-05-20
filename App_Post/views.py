from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Count
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from Login_App.models import UserProfile, Follow
from django.contrib.auth.models import User
from App_Post.models import Posts, Answer, Like
# Create your views here.


@login_required
def home(request):
    user = request.user
    if request.method == 'GET':
        search = request.GET.get('search',  ' ')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_Post/home.html', context={'title': 'Home', 'search': search, 'result': result, 'user': user})


@login_required
@login_required
def questions(request):
    posts = Posts.objects.all()
    return render(request, 'App_Post/question_list.html', context={'title': 'Frequently Asked Question', 'posts': posts})


@login_required
def add_ans(request, post_id):
    if request.method == 'POST':
        # Retrieve the post object based on the post_id
        post = Posts.objects.get(pk=post_id)
        author = request.user  # Get the logged-in user as the author
        # Get the comment content from the form submission
        content = request.POST['content']

        # Create a new Comment object and save it to the database
        ans = Answer(post=post, author=author, content=content)
        ans.save()

        # Redirect to the questions page after submitting the comment
        return redirect('App_Post:questions')

    # If the request method is GET, render the form to add a comment
    return render(request, 'App_Post/question_list.html')


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == 'POST':
        user = request.user
        liked_answers = Like.objects.filter(answer=answer, user=user)

        if liked_answers.exists():
            # User has already liked the answer, do not allow another like
            liked_answers.delete()
        else:
            # User has not liked the answer, add the like
            like = Like(answer=answer, user=user)
            like.save()

    return redirect('App_Post:questions')

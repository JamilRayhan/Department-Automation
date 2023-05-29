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
def questions(request):
    posts = Posts.objects.all()
    for post in posts:
        answers = post.comments.annotate(num_likes=Count('likes')).order_by('-num_likes')
        post.comments.set(answers)

    liked_answers = Like.objects.filter(user=request.user).values_list('answer', flat=True)
    context = {
        'title': 'Frequently Asked Question',
        'posts': posts,
        'liked_answers': liked_answers,
    }

    return render(request, 'App_Post/question_list.html', context=context)


@login_required
def add_ans(request, post_id):
    if request.method == 'POST':
        post = Posts.objects.get(pk=post_id)
        author = request.user 
        content = request.POST['content']

        ans = Answer(post=post, author=author, content=content)
        ans.save()
        return redirect('App_Post:questions')

    return render(request, 'App_Post/question_list.html')


@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == 'POST':
        user = request.user
        liked_answers = Like.objects.filter(answer=answer, user=user)

        if liked_answers.exists():

            liked_answers.delete()
        else:
            like = Like(answer=answer, user=user)
            like.save()

    return redirect('App_Post:questions')

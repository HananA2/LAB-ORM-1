from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post


def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    context = {
        'posts': posts
    }
    return render(request, 'blogger/home.html', context)


def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(
            title=title,
            content=content,
            is_published=True,
            published_at=timezone.now()
        )

        return redirect('home')

    return render(request, 'blogger/add_post.html')

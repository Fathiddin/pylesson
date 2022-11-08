from django.shortcuts import render, redirect
from .models import *
from .forms import CommentForm



def home(request):
    category = Category.objects.all()
    context = {
        'categories': category,
    }
    return render(request, 'index.html', context)


def category_post(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts,
    }
    return render(request, 'list.html', context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post = post
            instance.save()
            return redirect(f'/detail/{slug}')
    else:
        form = CommentForm()
    context = {
        'post': post,
        'form': form,
        'comments': comments
    }
    
    
    return render(request, 'post.html', context)




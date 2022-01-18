from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from django.core.paginator import Paginator
from django.db.models import Count
from posts.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/index.html'
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    template = 'posts/profile.html'
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
        'author': author,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    posts = get_object_or_404(Post, pk=post_id)
    title = posts.text[:30]
    author = posts.author
    date_my = Post.objects.annotate(post_count=Count('group'))
    context = {
        'posts': posts,
        'title': title,
        'author': author,
        'date_my': date_my,
    }
    return render(request, template, context)


def post_create(request):
    form = PostForm()
    groups = Group.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:profile', username=new_post.author.username)
        else:
            form = PostForm()
    context = {
        'form': form,
        'groups': groups,
    }
    return render(request, 'posts/create_post.html', context)


@login_required
def post_edit(request, post_id):
    is_edit = True
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.author = request.user
            post.pk = post_id
            post.text = form.cleaned_data['text']
            template = 'posts:post_detail'
            post.save()
            return redirect(template, post_id=post.pk)
    else:
        groups = Group.objects.all()
        form = PostForm(instance=post)
        template = 'posts/create_post.html'
        context = {
            'form': form,
            'groups': groups,
            'is_edit': is_edit,
        }
    return render(request, template, context)

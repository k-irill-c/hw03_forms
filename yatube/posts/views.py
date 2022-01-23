from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


from posts.utils import get_page_context
from .models import Post
from .models import Group
from .forms import PostForm
from posts.models import User


def index(request):
    context = get_page_context(
        Post.objects.all().order_by('-pub_date'), request
    )
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')
    context = {
        'group': group,
        'posts': posts,
    }
    context.update(get_page_context(posts, request))
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    template = 'posts/profile.html'
    context = {
        'author': author,
    }
    context.update(get_page_context(author.posts.all(), request))
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    posts = get_object_or_404(Post, pk=post_id)
    title = posts.text[:30]
    author = posts.author
    context = {
        'posts': posts,
        'title': title,
        'author': author,
    }
    return render(request, template, context)


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:profile', username=post.author.username)
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    groups = Group.objects.all()
    template = 'posts/create_post.html'
    is_edit = True
    form = PostForm(request.POST or None, instance=post)
    if post.author == request.user:
        if request.method == 'POST':
            if form.is_valid():
                post.pk = post_id
                post = form.save(commit=False)
                post.text = form.cleaned_data['text']
                template = 'posts:post_detail'
                post.save()
                return redirect(template, post_id=post.pk)
        context = {
            'form': form,
            'groups': groups,
            'is_edit': is_edit,
            'post': post,
        }
        return render(request, template, context)

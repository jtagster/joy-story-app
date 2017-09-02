from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.template.defaultfilters import slugify
from collection.forms import PostForm, NewPostForm, ShareForm
from collection.models import Post
from django.contrib.auth.decorators import login_required
from django.http import Http404

def index(request): 
    user = request.user
    posts = Post.objects.filter(user=user.id)
    # this is your new view - urls.py will catch that someone wants the homepage 
    #and points to this piece of code, which will render the index.html template.
    return render(request, 'index.html', {'posts': posts,})
@login_required
def feed(request): 
    #user = request.user
    #postsSelf = Post.objects.filter(user=user.id, public='PUBLIC', published_date__lte=timezone.now())
    posts = Post.objects.filter(public='PUBLIC', published_date__lte=timezone.now())
    #posts = (postsSelf | postsPublic).order_by('published_date')
        #ribbits_self = Ribbit.objects.filter(user=user.id)
        #ribbits_buddies = Ribbit.objects.filter(user__userprofile__in=user.profile.follows.all)
        #ribbits = ribbits_self | ribbits_buddies
    # this is your new view - urls.py will catch that someone wants the homepage 
    #and points to this piece of code, which will render the index.html template.
    return render(request, 'index.html', {'posts': posts,})
@login_required
def post_new(request):
    form_class = NewPostForm
    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            post = form.save(commit=False)

            # set the additional details
            post.user = request.user
            post.slug = slugify(post.title)
            # save the object
            post.save()

            # redirect to our newly created thing
            return redirect('post_detail', slug=post.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'post/post_new.html', {
        'form': form,
    })
@login_required
def post_detail(request, slug):
    # grab the object...
    post = Post.objects.get(slug=slug)
    form_class = ShareForm

    # if we're coming to this view from a submitted form,
    # do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('post_detail', slug=post.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=post)

    # and render the template
    return render(request, 'post/post_detail.html', {
        'post': post,
        'form': form,
    })
@login_required
def edit_post(request, slug):
    # grab the object...
    post = Post.objects.get(slug=slug)

    # make sure the logged in user is the owner of the thing
    if post.user != request.user:
        raise Http404

    # set the form we're using...
    form_class = PostForm

    # if we're coming to this view from a submitted form,
    # do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(data=request.POST, instance=post)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('post_detail', slug=post.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=post)

    # and render the template
    return render(request, 'post/edit_post.html', {
        'post': post,
        'form': form,
    })
@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.user != request.user:
        raise Http404
    post.publish()
    return redirect('post_detail', slug=slug) 
@login_required
def post_privacy(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.user != request.user:
        raise Http404
    if post.public == 'PRIVATE':
        post.share()
    else:
        post.unshare()
    return redirect('post_detail', slug=slug)  
@login_required
def post_draft_list(request):
    user = request.user
    posts = Post.objects.filter(user=user.id, published_date__isnull=True).order_by('created_date')
    return render(request, 'post/post_draft_list.html', {'posts': posts})
@login_required
def post_remove(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.user != request.user:
        raise Http404
    post.delete()
    return redirect('home')   
  
"""
There are a ton of different ways to display a template simply in the views, 
and my favorite is Django's shortcut function called render. This is something 
you'll need to import, but Django anticipates that you'll use it and already 
has it added to the top of views.py for us.
"""
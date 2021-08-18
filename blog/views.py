from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogForm


def display_blogcontent(request):

    blogposts = BlogPost.objects.all()
    template = 'blog/blog.html'
    context = {
        'blogposts': blogposts,
        }

    return render(request, template, context)


def show_post(request, slug):

    blogpost = get_object_or_404(BlogPost, pk=post_id)
    template = 'blog/show_post.html'
    context = {
        'blogpost': blogpost
        }
    return render(request, template, context)


@login_required
def add_post(request):
    """ Adds a new post to our blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, f'Successfully added {post.title}!')
            return redirect(reverse('show_post', args=[post.id]))
        else:
            messages.error(request,
                           'Failed to add post to our blog.'
                           'Please check if the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_post.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, post_id):
    """ Edit the post in our blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {post.title}!')
            return redirect(reverse('show_post', args=[post.id]))
        else:
            messages.error(request, f'Failed to update {post.title}.\
                                     Please check if the form is valid.')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """ Deletes the post from our blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the admin can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    messages.success(request, f'{post.title} was successfully deleted!')
    return redirect(reverse('display_blogcontent'))

from django.shortcuts import render
from .models import BlogPost


def blogcontent(request):

    blogposts = BlogPost.objects.all()
    template = 'blog/blog.html'
    context = {
        'blogposts': blogposts,
        }

    return render(request, template, context)
    
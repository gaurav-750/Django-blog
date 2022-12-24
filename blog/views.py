from django.shortcuts import render
from django.views.generic import ListView,  DetailView
from .models import Post


# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'blog'  # the object which we r sending

from django.shortcuts import render
from django.views.generic import ListView,  DetailView, CreateView, UpdateView
from .models import Post

from django.urls import reverse, reverse_lazy


# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'blog'  # the object which we r sending


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'  # all fields in the model will be included by default
    # fields = ('title', 'body') #  only these fields will be included

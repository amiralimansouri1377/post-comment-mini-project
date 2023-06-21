from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views import View
from .models import Post, Comment
from .form import CommentForm

# Create your views here.
class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"


class PostDetailView(DetailView):
    template_name = "blog/detail-post.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CommentForm()
        context["form"] = form
        return context
    

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = Post.objects.get(slug=self.kwargs.get("slug"))
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        self.success_url = f"/posts/{self.kwargs.get('slug')}"
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return super().get_success_url()
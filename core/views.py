from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *  # TemplateView, ListView
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm


# bad practice to use functions

# def home(request):
#     return HttpResponse('<h1>Home page!</h1>'
#                         '<a href="/about/">About</a>')
#
#
# def about(request):
#     return HttpResponse('<h1>About page!!</h1>'
#                         '<a href="/home/">Home</a>'
#                         '<br></br>'
#                         '<a href="/test/">test</a>')
#
#
# def test(request):
#     return render(request, './frontend/index.html', {})

# better is to use classes 'Classy Class-Based Views.' https://ccbv.co.uk

# posts = [
#     {'title': 'How to learn Python', 'author': 'admin', 'data': '12345678'},
#     {'title': 'How to learn Java', 'shy': 'admin', 'data': '124587963'},
#     {'title': 'How to learn cmd', 'author': 'admin', 'data': '224857566'},
# ]


class AboutView(TemplateView):
    """ Base About view """
    template_name = 'core/about.html'


class HomeView(ListView):
    """ Base Home view """
    template_name = 'core/home.html'
    # queryset = [1, 2, 3]
    # queryset = Post.objects.all()
    # queryset = Post.objects.values()
    # queryset = Post.objects.values('title', 'body')
    # queryset = Post.objects.values('title', 'body', 'image')
    # queryset = Post.objects.all()

    # for sorted view of posts on home page need change queryset
    queryset = Post.objects.all().order_by('-updated_at')

    # def get(self, request):
    #     return super().get(request)


class PostDetailView(DetailView):
    template_name = 'core/post_detail.html'
    model = Post
    pk_url_kwarg = 'id'


# class PostDetailView(TemplateView):
#     template_name = 'core/post_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = Post.objects.get(id=context['id'])
#         context['post'] = post
#         return context

class PostCreateView(CreateView):
    template_name = 'core/post_create.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('core:home_page')


class PostDeleteView(DeleteView):
    template_name = 'core/post_delete.html'
    model = Post
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('core:home_page')


class CommentCreateView(CreateView):
    template_name = 'core/add_comment.html'
    model = Comment
    form_class = CommentForm
    pk_url_kwarg = 'id'

    success_url = ''

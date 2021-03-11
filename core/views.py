from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Post, Comment

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

posts = [
    {'title': 'How to learn Python', 'author': 'admin', 'data': '12345678'},
    {'title': 'How to learn Java', 'shy': 'admin', 'data': '124587963'},
    {'title': 'How to learn cmd', 'author': 'admin', 'data': '224857566'},
]


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
    queryset = Post.objects.all()

    # def get(self, request):
    #     return super().get(request)

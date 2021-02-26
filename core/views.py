from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home page!</h1>'
                        '<a href="/core/about/">About</a>')


def about(request):
    return HttpResponse('<h1>About page!!</h1>'
                        '<a href="/core/home/">Home</a>'
                        '<br></br>'
                        '<a href="/core/test/">test</a>')


def test(request):
    return render(request, './frontend/index.html', {})

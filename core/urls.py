from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about_page'),
    path('home/', views.HomeView.as_view(), name='home_page'),
    # path('test/', views.test, name='test_page'),
]

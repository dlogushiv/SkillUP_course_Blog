from django.urls import path
from . import views

# if we have many applications, it is better to use namespases
# create variable 'app_name = <application name>'
# and after that use <a href="{% url 'app_name:page_name' %}">link text</a>
# in template pages
app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('about/', views.AboutView.as_view(), name='about_page'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create_page'),
    path('post_detail/<int:id>/', views.PostDetailView.as_view(), name='post_detail_page'),
    path('post_detail/<int:id>/delete/', views.PostDeleteView.as_view(), name='post_delete_page'),
    path('post_detail/<int:id>/add_comment/', views.CommentCreateView.as_view(), name='add_comment_page'),
]
# if we have not many applications/pages, we can not to use namespases
# no need a variable 'app_name = <application name>'
# and use <a href="{% url 'page_name' %}">link text</a> # in template pages

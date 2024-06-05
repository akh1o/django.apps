from django.urls import path
from . import views

app_name = 'blogapi'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view, name='detail'),
	path('create/', views.createBlog, name='create_blog'),
	path('delete/<int:blog_id>/', views.deleteBlog, name='delete_blog')
]
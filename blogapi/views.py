from django.shortcuts import render
from .models import Blog
from django.utils import timezone

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'blogapi/index.html'
	
	def get_query_set(self):
		return Blog.objects.filter(pub_date__lte=timezone.now())


class DetailView(generic.DetailView):
	template_name = 'blogapi/detail.html'
	model = Blog

	def get_query_set(self):
		return Blog.objects.filter(pub_date__lte=timezone.now())

def createBlog(request):
	if request.method == 'POST':
		data = request.POST
		b = Blog(data)
		b.save()

def deleteBlog(request, blog_id):
	Blog.objects.filter(id=blog_id).delete()






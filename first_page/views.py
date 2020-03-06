from django.shortcuts import render
from django.http import HttpResponse


posts = [
		{
			'author' : 'Thirumalai',
			'title'	: 'My first post',
			'content' : 'First post is interesting',
			'date' : 'February 02,2020',
		},
		{
			'author' : 'Vinayagan',
			'title'	: 'My second post',
			'content' : 'Second post is interesting',
			'date' : 'February 10,2020',
		}
	]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html')


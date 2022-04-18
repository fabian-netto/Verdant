from urllib import request
from django.shortcuts import render
from .models import *

# Create your views here.
def about(request):
    return render(request, 'about.html')  

def blogdetails(request,pk):
    pr = Blog.objects.get(blog_id=pk)
    context = {'pr':pr}
    return render(request, 'blog-details.html', context) 

def contact(request):
    return render(request, 'contact.html')   

def news(request):
    return render(request, 'news.html')   

def solutionsdetails(request):
    return render(request, 'solutions-details.html')   

def blog(request):
    pro = Blog.objects.all()
    context = {'pro':pro}
    return render(request, 'blog.html', context)         
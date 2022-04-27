from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from learning.views  import *

# Create your views here.
def about(request):
    return render(request, 'about.html')  

def blogdetails(request,pk):
    pr = Blog.objects.get(blog_id=pk)
    pb = Blog.objects.all()
    context = {'pr':pr,'pb':pb}
    return render(request, 'blog-details.html', context) 

def contact(request):
    return render(request, 'contact.html')   

def news(request):
    return render(request, 'news.html')   

def solutionsdetails(request,pk):
    cou = Course.objects.get(course_id=pk)
    context = {'cou':cou}
    return render(request, 'solutions-details.html' ,context)   

def blog(request):
    pro = Blog.objects.all()
    context = {'pro':pro}
    return render(request, 'blog.html', context)    

def register(request):
    if request.method == 'POST':
        a=registerform(request.POST)
        if a.is_valid():
            name=a.cleaned_data['name']
            email=a.cleaned_data['email']
            number=a.cleaned_data['number']
            subject=a.cleaned_data['subject']
            message=a.cleaned_data['message']

           
            b=Registrationform(name=name,email=email,number=number,subject=subject,message=message)
            b.save()
            return redirect(index)
        else:
            return HttpResponse('registration incomplte')
    else:
        return render(request,'index.html')    

def privacy(request):
    return render(request, 'privacy.html')

def react(request):
    return render(request, 'react.html') 

def java(request):
    return render(request, 'java.html')  

def angular(request):
    return render(request, 'angular.html')  

def quantum(request):
    return render(request, 'quantum.html')    

def ai(request):
    return render(request, 'ai.html') 

def edge(request):
    return render(request, 'edge.html')                       

def coursedetails(request):
    cor = Course.objects.all()
    context = {'cor':cor}
    return render(request, 'course-details.html',context)  
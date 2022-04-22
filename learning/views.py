from django.shortcuts import render
from blog.models import *

def index(request):
    cou = Course.objects.all()
    blo = Blog.objects.all()
    context = {'cou':cou,'blo':blo}
    
    return render(request, 'index.html', context)


from django.shortcuts import render
from blog.models import *

def index(request):
    cou = Course.objects.all()
    context = {'cou':cou}
    return render(request, 'index.html', context)


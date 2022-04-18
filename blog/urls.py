from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/',views.about,name='about'),  
    path('blog/',views.blog,name='blog'), 
    path('blogdetails/<str:pk>/',views.blogdetails,name='blogdetails'),
    path('contact/',views.contact,name='contact'), 
    path('news',views.news,name='news'), 
    path('solutionsdetails/',views.solutionsdetails,name='solutionsdetails'),    
]

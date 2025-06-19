import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
import markupsafe
from myINT.forms import LogMessageForm
from myINT.models import Blog, Category
from django.views.generic import ListView
import markdown
from django.utils.safestring import mark_safe

def index(request):
    
    return render(request, "myINT/home.html")

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'myINT/blog.html',{'blogs': blogs})

def case(request):
   
    return render(request, 'myINT/caseStudies.html')

def joinus(request):
    team_members = [
        {
            'name': 'David',
            'role': 'CEO at iNT Solutions',
            'image': 'myINT/images/David.png'
        },
        {
            'name': 'Peter',
            'role': 'CTO at iNT Solutions',
            'image': 'myINT/images/peter.png'
        },
        {
            'name': 'Rachel',
            'role': 'Lead Designer',
            'image': 'myINT/images/rachel.png'
        },
        {
            'name': 'Ryan',
            'role': 'Lead Developer',
            'image': 'myINT/images/ryan.png'
        }
    ]
    return render(request, 'myINT/joinUs.html', {'team_members': team_members})

def blog_detail(request, blog_id):
   blog = get_object_or_404(Blog, id=blog_id)
   html_content = markdown.markdown(blog.content)
   print(markdown.markdown(blog.content))
   return render(request, 'myINT/blogdetail.html', {'blog': blog,'html_content': html_content})
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
    blogs = Blog.objects.all()
    return render(request, "myINT/home.html", {'blogs': blogs})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'myINT/blog.html',{'blogs': blogs})

def case(request):
    blogs = Blog.objects.all()
    return render(request, 'myINT/caseStudies.html', {'blogs': blogs})

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
    # Get the current blog (with 404 if not found)
    blog = get_object_or_404(Blog, id=blog_id)

    # Convert Markdown content to HTML
    content_with_image = blog.content.replace("$BLOG_IMAGE_URL$", blog.image.url)
    # Replace placeholder in Markdown with actual image URL
    html_content = markdown.markdown(content_with_image)
    # Find related blogs based on categories (exclude current blog)
    related_blogs = Blog.objects.filter(
        categories__in=blog.categories.all()
    ).exclude(id=blog.id).distinct()[:3]  # Limit to 3 related blogs

    # Prepare context for template
    context = {
        'blog': blog,
        'html_content': html_content,
        'related_blogs': related_blogs,
        # Mark as safe for rendering HTML
    }

    return render(request, 'myINT/blogdetail.html', context)
import os
from django.contrib import messages
from django.urls import reverse
from django.utils.timezone import datetime
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
import markupsafe
from myINT.forms import LogMessageForm
from myINT.models import Blog, Category
from django.views.generic import ListView
import markdown
from django.utils.safestring import mark_safe
from django.core.mail import send_mail

from web_django import settings

def index(request):
    blogs = Blog.objects.all()
    return render(request, "myINT/home.html", {'blogs': blogs})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'myINT/blog.html',{'blogs': blogs,'current_page': 'blog'})

def case(request):
    blogs = Blog.objects.all()
    return render(request, 'myINT/caseStudies.html', {'blogs': blogs,'current_page': 'casestudies'})

def joinus(request):
    
    return render(request, 'myINT/joinus.html', { 'current_page': 'joinus'})

def blog_detail(request, blog_id):
    # Get the current blog (with 404 if not found)
    blog = get_object_or_404(Blog, id=blog_id)

    # Increment view count
    blog.view_count += 1
    blog.save(update_fields=['view_count'])
    print(f"View count incremented to: {blog.view_count}")
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
    }

    return render(request, 'myINT/blogdetail.html', context)

def download_company_profile(request):
    file_path = os.path.join(os.path.dirname(__file__), 'ints-profile.pdf')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')

def contact_us(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        category = request.POST.get('category')
        message = request.POST.get('message')

        full_message = f"""
New Contact Message

Name: {name}
Company: {company}
Email: {email}
Phone: {phone}
Category: {category}
Message: {message}
        """

        send_mail(
            subject=f"New Contact Us Message from {name}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=settings.CONTACT_US_EMAIL_RECIPIENTS, 
            fail_silently=False,
        )

        # Add success message to context
        messages.success(request, "✅ Your message has been sent successfully.")
        url = reverse('home') + '#contact'
        return redirect(url)
    return render(request, "myINT/home.html", context)  
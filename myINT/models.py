from django.db import models
from django.utils import timezone
from django.urls import reverse
from jsonschema import ValidationError



class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Returns a string representation of the category."""
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True) 
    categories = models.ManyToManyField('Category', blank=True)
    image = models.FileField(upload_to='blog_images/', blank=True, null=True)
    tags = models.ManyToManyField('Tag', related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)
    
   
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'categories': self.categories.name if self.categories else None,
            'image': self.image.url if self.image else None,
            'view_count': self.view_count,
        }
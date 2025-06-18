from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from django_summernote.fields import SummernoteTextField


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
        return self.name
    


class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True) # You can paste raw HTML here
    # OR use RichTextField for WYSIWYG editor:
    # content = RichTextField()
    categories = models.ManyToManyField(Category, related_name='blogs', blank=True)
    def __str__(self):
        return self.title
from django.contrib import admin
from .models import Blog, Category
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'get_categories')

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    
    get_categories.short_description = 'Categories'  # Optional: set column header name

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
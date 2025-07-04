# Generated by Django 4.2.16 on 2025-06-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myINT', '0003_remove_blog_category_blog_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='myINT.category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]

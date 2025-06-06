import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from myINT.forms import LogMessageForm
from myINT.models import LogMessage
from django.views.generic import ListView


def index(request):
    
    return render(request, "myINT/home.html")

def about(request):
    return render(request, 'myINT/about.html')
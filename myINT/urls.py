from django.urls import path
from myINT import views
from myINT.models import LogMessage



urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.index, name="home"),
    path('blog/', views.blog, name='blog'),
   

]


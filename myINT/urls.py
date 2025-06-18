from django.urls import include, path
from myINT import views
from myINT.models import LogMessage



urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.index, name="home"),
    path('blog/', views.blog, name='blog'),
    path('casestudies/', views.case, name='case'),
    path('joinus/', views.joinus, name='joinus'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    

]


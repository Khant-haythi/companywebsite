from django.urls import include, path
from myINT import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from myINT.models import LogMessage
from web_django import settings



urlpatterns = [
    path("", views.index, name="home"),
    path("home/", views.index, name="home"),
    path('blog/', views.blog, name='blog'),
    path('casestudies/', views.case, name='case'),
    path('joinus/', views.joinus, name='joinus'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('profile.pdf', views.download_company_profile, name='download_profile'),
    path('contact/', views.contact_us, name='contact_us'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

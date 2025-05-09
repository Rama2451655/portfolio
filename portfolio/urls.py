from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('download_resume/', views.download_resume, name='download_resume'),
    path('', views.resume_view, name='resume'), 
]

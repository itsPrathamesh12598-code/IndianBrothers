from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('careers/', views.careers, name='careers'),
    path('casestudies/', views.caseStudies, name='casestudies'),
    path('insights/', views.inSights, name='insights'),
    path('expertise/', views.expertise, name='expertise'),
    path('services/', views.services, name='services'),
    path('about/', views.aboutInfo, name='about'),
]

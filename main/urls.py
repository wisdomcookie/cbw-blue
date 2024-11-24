from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('join/volunteer/', views.volunteer, name='volunteer'),
    path('join/careers/', views.hiring, name='hiring'),
    path('locations/<str:shopname>/', views.shop, name='shops'),
    path('about/impact/', views.impact, name='impact'),
    path('about/people/', views.people, name='people'),
    path('about/programs/', views.programs, name='programs'),
    
]

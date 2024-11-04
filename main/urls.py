from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('programs/', views.programs, name='programs'),
    path('shops/<str:shopname>/', views.shop, name='shops'),
    path('about/mission/', views.mission, name='mission'),
    path('about/people/', views.people, name='people'),
    path('about/hiring/', views.hiring, name='hiring'),
    
]

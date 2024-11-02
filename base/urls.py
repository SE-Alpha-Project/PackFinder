from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('messages/', views.inbox, name='messages'),
    path('quiz/', views.compatibility_quiz, name='quiz'),
    path('find-people/', views.find_people, name='find-people'),
] 
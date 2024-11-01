from django.urls import path
from . import views

urlpatterns = [
    # ... your other URL patterns ...
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
] 
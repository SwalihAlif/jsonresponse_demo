from django.urls import path
from . import views


urlpatterns = [
    path('sweet/', views.sweet_feedback, name='sweet_feedback'),
    path('', views.sweet_page, name='sweet_page'),
    
]
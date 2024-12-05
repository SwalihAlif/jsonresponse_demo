from django.urls import path
from . import views


urlpatterns = [
    path('csrf/', views.submit_feedback, name='submit_feedback'),
    path('', views.show_page, name='sample_json'),
    
]
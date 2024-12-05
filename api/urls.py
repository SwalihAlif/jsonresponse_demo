from django.urls import path
from . import views

urlpatterns = [
    path('json/', views.sample_json_response, name='sample_json')
]
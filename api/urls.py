from django.urls import path
from . import views


urlpatterns = [
    path('json/', views.sample_json_response, name='sample_json'),
    path('my_json_view/', views.my_json_view, name='my_json_view'),
    path('', views.show_json_form, name='show_form'),
]
from django.urls import path

from api import views

urlpatterns = [
    path('register/', views.register_address, name='register'),
    path('get_all/', views.get_all_address, name='get_all'),
    path('get_location/', views.get_location, name='get_location'),
]


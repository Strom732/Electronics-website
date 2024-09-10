from django.urls import path
from . import views

urlpatterns = [

    path('services/', views.services, name='services')


    # define your URL patterns here
]
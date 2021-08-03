from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('aranjamente/', views.aranjamente, name='arangamente'),
    path('evenimente/', views.evenimente, name="evenimente")
]
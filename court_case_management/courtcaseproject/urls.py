from django import urls, views
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('registration', views.register),
    path('login', views.login),
    path('services', views.services),
    path('contact_us', views.contact_us),
    path('about_us', views.about_us),
    path('portfolio', views.portfolio),
    path('blog', views.blog),
    path('presearchclient', views.presearchclient),
    path('searchclients', views.searchclients),
    path('allclient', views.allclient),
    path('upadateclient/<str:pk>', views.updateclient, name="update"),
    path('deleteUser/<str:pk>', views.deleteUser, name="delete"),
    path('admindashboard', views.adminboard),
]
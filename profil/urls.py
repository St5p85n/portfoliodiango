from django.urls import path
from profil.views import *
urlpatterns = [
    path('',inscriptionForm,name='inscriptionForm'),
    path('ajoutUtil/',inscription,name='ajoutUtil'),
    path('loginForm/',loginForm,name='loginForm'),
    path('login/',seConnecter,name='login'),
    path('logout/',logoutUser,name='logout'),
]
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from profil.models import Utilisateur

user = get_user_model()
# Create your views here.
def inscriptionForm(request):
    return render(request,'profil/register.html')

def loginForm(request):
    return render(request,'profil/login.html')
def seConnecter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('login')
        else:
            return redirect('login')
    return render(request,'profil/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
def inscription(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        telephone = request.POST.get('telephone')
        address = request.POST.get('address')
        user.objects.create_user(username=username, last_name=last_name, email=email,password=password,telephone=telephone,address=address)
    return redirect('inscriptionForm')
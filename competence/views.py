from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from rest_framework import viewsets

from competence.models import Categorie
from competence.serializers import CategoriSerializer


class CategorieView(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategoriSerializer

# Create your views here.
def index(request):
    return HttpResponse("<h1 style='color:green;text-align:center'>WELCOME ON THE BOARD</h1>")

def accueil(request):
    """ 1 - Debutant 2- Intermediaire - 3 Expert """

    paginator = Paginator(Categorie.objects.all(),3)
    page = request.GET.get('page')
    categories = paginator.get_page(page)
    return render(request,'competence/categorie/accueil.html',{'cats':categories})

def liste(request):
    return render(request,'competence/liste.html')

def addCategorie(request):
    if request.method == 'POST':
        libelle = request.POST['libelle']
        description = request.POST['description']
        Categorie.objects.create(libelle=libelle,description=description)
    return redirect("accueil")

def deleteCategorie(request,id):
    categorie = get_object_or_404(Categorie,id=id)
    categorie.delete()
    return redirect("accueil")
def modifCategorie(request,id):
    categorie = get_object_or_404(Categorie,id=id)
    return render(request,'competence/categorie/update.html',{'cat':categorie})
def updateCategorie(request):
    if request.method == 'POST':
        categorie = get_object_or_404(Categorie,id=request.POST['id'])
        categorie.libelle = request.POST['libelle']
        categorie.description = request.POST['description']
        categorie.save()
    return redirect("accueil")
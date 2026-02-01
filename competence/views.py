from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1 style='color:green;text-align:center'>WELCOME ON THE BOARD</h1>")

def accueil(request):
    """ 1 - Debutant 2- Intermediaire - 3 Expert """
    competences = [
        {
            'nom':'Django',
            'description':'integration template',
            'niveau':1,
        },
        {
            'nom': 'JEE',
            'description': 'Web services starter',
            'niveau': 2,
        },
        {
            'nom': 'BD',
            'description': 'BD Relationnelle',
            'niveau': 2,
        }
    ]
    return render(request,'competence/accueil.html',{'competences':competences})

def liste(request):
    return render(request,'competence/liste.html')
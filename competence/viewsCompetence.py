from django.shortcuts import render, get_object_or_404, redirect

from competence.models import Categorie, Competence


def accueilCompetence(request):
    categories = Categorie.objects.all()
    competences = Competence.objects.all()
    return render(request, "competence/comp/addliste.html",{'categories':categories,'competences':competences})

def addCompetence(request):
    if request.method == "POST":
        libelle =request.POST['libelle']
        description = request.POST['description']
        categori = get_object_or_404(Categorie, id=request.POST['categori'])
        niveaux = request.POST['niveaux']
        Competence.objects.create(libelle=libelle,description=description,niveaux=niveaux,categori=categori)
    return redirect("competence")
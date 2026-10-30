from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login
from django.urls import reverse
from .models import Test, RecetteIngredient, Recette, Ingredient
from django import forms
#from .forms import Newpost
from django.contrib.auth.models import User
from . import models
import numpy as np

# Create your views here.

def index(request):
   return HttpResponse(render(request,"recettes/index.html", context = { 'dbrecette': Recette.objects.all()[:3]}))


def about(request):
   return HttpResponse(render(request,"recettes/about.html"))
def menu(request):
   return HttpResponse(render(request,"recettes/menu.html",  context = { 'dbrecette': Recette.objects.all()}))


from .forms import RecetteForm

def ajout_recette(request):
   '''
   Args:
        requette http
 
    Returns:
        reponse http
   '''
   if request.method == "GET":
      return HttpResponse(render(request,"recettes/ajout_recette.html", {"form":RecetteForm, "ingr":Ingredient.objects.all()}))
   elif request.method == "POST":
      form = RecetteForm(request.POST, request.FILES)
      li = [int(key) for key, value in request.POST.items() if (value == 'on' and key != 'four')]
      if form.is_valid():
         recipe = form.save(commit=False)
         recipe.creator = request.user
         recipe.save()
            
         for ingred in li:
            newlink = RecetteIngredient(recette=recipe, ingredient=[elem for elem in Ingredient.objects.all() if elem.id==ingred][0])
            newlink.save()
            
         return redirect(reverse("index"))
      return HttpResponse(render(request,"recettes/ajout_recette.html", {"form":RecetteForm, "ingr":Ingredient.objects.all()}))




      
      


def resultats(request):
   ''' Retourne les recettes que peut réaliser l'utilisateur à partir de ingrédients qu'il possède. 
   Args:
        requette http
 
    Returns:
        reponse http
   '''
   li = [int(key) for key, value in request.POST.items() if value == 'on']
   ingredients_users=[elem for elem in Ingredient.objects.all() if elem.id in li]
   recettes_compatibles = []
   template = loader.get_template("recettes/resultats.html")

   for recettee in models.Recette.objects.all() :
      dedans = True
      for lien in models.RecetteIngredient.objects.all() :
         if lien.recette == recettee:
            if not lien.ingredient in ingredients_users:
               dedans = False
      if dedans is True :
         recettes_compatibles.append(recettee)
   context = {
      'recettes' : recettes_compatibles
   }
   return HttpResponse(template.render(context, request))


def recherche(request):
   return HttpResponse(render(request,"recettes/recherche.html/", {'ingr':Ingredient.objects.all()}))

 



## Fonctions utiles à la recherche classique ##
def DetailRecette(request, recette_id):
   ''' Crée une vue qui donne les détails de la recette (étapes clés)
   Args:
        requette http
        identifiant de la recette
 
    Returns:
        reponse http
   '''
   template_name = "recettes/detail_recette.html"
   recette = get_object_or_404(Recette, id=recette_id)

   context = {
        'recette': recette,
    }

   return render(request, template_name, context)
 

def PageDeRecherche(request):
    '''Crée une vue pour la page de recherche de recette
    Args:
        requette http
 
    Returns:
        reponse http
   '''
    template_name = "recettes/pageRecherche.html"
    results_template = "recettes/resultats_recherche.html"

    query = request.GET.get('q')
    results = []

    if query:
        results = Recette.search(query)

        # Redirige vers la page des résultats avec le contexte
        return render(request, results_template, {'results': results, 'query': query})

    context = {
        'query': query,
    }

    return render(request, template_name, context)

def ResultatsRecherche(request):
    ''' Crée une vue qui liste toute les recettes correspondant à la recherche
      Args:
        requette http
 
    Returns:
        reponse http
   '''
    template_name = "recettes/resultats_recherche.html"

    query = request.GET.get('q')
    results = []

    if query:
        # Recherche toutes les recettes qui contiennent la chaîne de caractères dans le titre ou la description
        results = Recette.objects.filter(title__icontains=query) | Recette.objects.filter(description__icontains=query)

    context = {
        'results': results,
        'query': query,
    }

    return render(request, template_name, context)

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
import django.contrib.auth
from django.urls import reverse
from recettes.forms import CustomUserCreationForm
from recettes.models import Recette

# Create your views here.

def login(request):
    ''' Crée une vue pour quand l'utilisateur est connecté et pour afficher ses recettes par la suite
   Args:
        requette http
 
    Returns:
        reponse http
   '''
    return HttpResponse(render(request,"recettes/login.html", {'dbrecette': [recette for recette in Recette.objects.all() if recette.creator == request.user]}))

def register(request):
    ''' Crée la vue de la page de création d'un compte
   Args:
        requette http
 
    Returns:
        reponse http
   '''
    if request.method == "GET":
        return render(
            request, "recettes/register.html",
            {"form": CustomUserCreationForm }
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            django.contrib.auth.login(request, user)
            return redirect(reverse("index"))
        return render(
            request, "recettes/register.html",
            {"form": CustomUserCreationForm }
        )
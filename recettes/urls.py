from django.urls import path, re_path, reverse
from django.shortcuts import redirect
import recettes.views

urlpatterns = [
    path("",recettes.views.index, name="index"),
    path("about/",recettes.views.about, name="about"),
    path("menu/",recettes.views.menu, name="menu"),
    path("ajout-recette/", recettes.views.ajout_recette, name="ajout"),
    path("recherchee/", recettes.views.recherche, name ='recherche'),
    path("resultatss/", recettes.views.resultats, name ='resultats'),
    path('recherche/', recettes.views.PageDeRecherche, name='PageDeRecherche'),
    path('resultats/', recettes.views.ResultatsRecherche, name='ResultatsRecherche'),
    path('detail/<int:recette_id>/', recettes.views.DetailRecette, name='detail_recette'),
]





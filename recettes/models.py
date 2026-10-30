from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

# Create your models here.

class Recette(models.Model):
    title= models.CharField(max_length=200)
    photo= models.ImageField(upload_to="recettes/static/img_recettes/", blank=True, null=True)
    four= models.BooleanField()
    
    types_choices = [
        ("Végétarien", "Végétarien"),
        ("Pesco-végétarien", "Pesco-végétarien"),
        ("Végétalien", "Végétalien"),
        ("Végan", "Végan"),
        ("Halal", "Halal"),
        ("Casher", "Casher"),
    ]
    type = models.CharField(max_length=20, choices=types_choices, blank=True, null=True)
    
    description = models.TextField()
    
    creator =models.ForeignKey(User, on_delete=models.CASCADE)
    
    favoris = models.ManyToManyField(User, related_name='recettes_favoris', blank=True)
    commentaires = models.ManyToManyField(User, through='Commentaire', related_name='recettes_commentees', blank=True)
    notes = models.ManyToManyField(User, through='Note', related_name='recettes_notees', blank=True) 
    
    def __str__(self):
        return self.title
    
    def search(query):
        exact_match = Recette.objects.filter(title__iexact=query).first()

        if exact_match:
            # S'il y a une correspondance exacte, retournez cette recette
            return [exact_match]
        else:
            # Sinon, effectuez une recherche partielle
            return Recette.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            ).distinct()
        
class Commentaire(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    commentaire = models.TextField()

class Note(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    note = models.IntegerField(choices=[(i, str(i)) for i in range(6)])

class Ingredient(models.Model):
    nom = models.CharField(max_length=255)
    empreintecarbone = models.FloatField(blank=True, null=True)
    recettes_ingredients = models.ManyToManyField(Recette, through='RecetteIngredient', related_name='recettes_ingredients') 
    
    def __str__(self):
        return self.nom

class RecetteIngredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.FloatField(blank=True, null=True)
    
    
class Test(models.Model): #inutile était là pour des tests
    text=models.CharField(max_length=30)
    creator =models.ForeignKey(User, on_delete=models.CASCADE)
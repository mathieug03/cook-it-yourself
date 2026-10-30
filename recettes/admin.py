from django.contrib import admin

# Register your models here.
from .models import Recette, Ingredient, Commentaire, Note, RecetteIngredient, Test

admin.site.register(Recette)
admin.site.register(Ingredient)
admin.site.register(Commentaire)
admin.site.register(Note)
admin.site.register(RecetteIngredient)
admin.site.register(Test)

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Recette, RecetteIngredient, Ingredient

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email","first_name","last_name")

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['title', 'photo', 'four', 'type', 'description']
        

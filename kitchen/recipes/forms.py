from django import forms
from django.forms import ModelForm, Textarea

from .models import Recipe

class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'ingredient-input', 'rows': 1}))
    directions = forms.CharField(widget=forms.Textarea(attrs={'class': 'direction-input', 'rows': 10}))

    class Meta:
        model = Recipe
        fields = [
            'name', 'short_description', 'image', 'prep_time', 'cook_time', 'freeze_time',
            'cool_time', 'total_time', 'servings', 'tips',
            'calories', 'fat', 'carbs', 'protein'
        ]

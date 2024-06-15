from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name', 'short_description','category', 'image_url', 'prep_time', 'cook_time', 'freeze_time',
            'cool_time', 'total_time', 'servings', 'tips',
            'calories', 'fat', 'carbs', 'protein'
        ]


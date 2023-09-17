from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

    rating = forms.IntegerField(
        validators=[
            MinValueValidator(1, 'Rating must be at least 1.'),
            MaxValueValidator(5, 'Rating must be at most 5.')
        ]
    )

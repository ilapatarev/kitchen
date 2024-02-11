from django.conf import settings
from django.db import models
from django.urls import reverse

from kitchen.recipes.models import Recipe
from kitchen.accounts.models import KitchenUser, Profile


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Add a field for the rating (e.g., 1 to 5 stars)
    comment = models.TextField(blank=True)  # Add a field for the comment
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.email} for {self.recipe.name}"

    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])
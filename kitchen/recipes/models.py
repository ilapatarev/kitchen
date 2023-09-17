from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipe_images/', max_length=5000000, blank=True)
    prep_time = models.IntegerField( default=0)
    cook_time = models.IntegerField( default=0)
    freeze_time = models.IntegerField( default=0)
    cool_time = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)
    servings = models.PositiveIntegerField(default=1)
    ingredients = ArrayField(models.CharField(max_length=200))  # ArrayField for ingredients
    directions = ArrayField(models.TextField())
    tips = models.TextField()
    calories = models.PositiveIntegerField(default=0)  # Default value
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Default value
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Default value
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Default value

    def __str__(self):
        return self.short_description

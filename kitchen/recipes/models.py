from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings
from django.db.models import Avg




class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    short_description = models.CharField(max_length=200)
    CATEGORY_CHOICES = [
	    ( 'Cakes', 'Cakes'),
	    ('Ice creams', 'Ice creams'),
        ('Cookies', 'Cookies'),
        ('Candies', 'Candies'),
        ('Pies', 'Pies'),
        ('Tarts', 'Tarts'),
        ('Pouddings', 'Pouddings'),
        ('Vegan', 'Vegan'),
        ('Other', 'Other'),

    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    image_url = models.URLField(max_length=200, blank=True, null=True)
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

    def average_rating(self):
        from kitchen.review.models import Review
        # Calculate and return the average rating for this recipe
        avg_rating= Review.objects.filter(recipe=self).aggregate(Avg('rating'))['rating__avg']
        if avg_rating:
            return round(avg_rating, 1)


    def __str__(self):
        return self.short_description

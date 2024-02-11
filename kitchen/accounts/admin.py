from django.contrib import admin

# Register your models here.

from django.contrib import admin
from ..recipes.models import Recipe
from ..review.models import Review
from .models import KitchenUser, Profile

# Register your models here



class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')




admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(KitchenUser)
admin.site.register(Profile)

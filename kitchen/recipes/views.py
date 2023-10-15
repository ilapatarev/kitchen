from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RecipeForm
from .models import Recipe
from ..review.forms import ReviewForm
from ..review.models import Review


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user

            # Extract ingredients and directions from POST data
            ingredients = []
            directions = []
            for key, value in request.POST.items():
                if key.startswith('ingredients_'):
                    ingredients.append(value)
                elif key.startswith('directions_'):
                    directions.append(value)

            recipe.ingredients = ingredients
            recipe.directions = directions

            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()

    return render(request, 'recipes/add_recipe.html', {'form': form})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    user_has_reviewed = False
    average_rating = None
    review_form = None  # Initialize the review_form variable

    if request.user.is_authenticated:
        user_has_reviewed = Review.objects.filter(recipe=recipe, user=request.user).exists()

        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                if user_has_reviewed:
                    # User has already left a review
                    return render(request, 'recipes/recipe_detail.html', {
                        'recipe': recipe,
                        'user_has_reviewed': user_has_reviewed,
                        'review_form': review_form,  # Pass the form even if it's not used
                    })
                else:
                    # Save the new review
                    review = review_form.save(commit=False)
                    review.user = request.user
                    review.recipe = recipe
                    review.save()
                    return redirect('recipe_detail', pk=recipe.pk)
        else:
            review_form = ReviewForm()

        # Calculate the average rating
        # average_rating = Review.objects.filter(recipe=recipe).aggregate(Avg('rating'))['rating__avg']


    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'user_has_reviewed': user_has_reviewed,
        'review_form': review_form,  # Always pass the review_form
        # 'average_rating': average_rating,
    })


@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Check if the logged-in user is the owner of the recipe
    if request.user != recipe.user:
        return redirect('home')  # Redirect to recipe detail if not the owner

    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')  # Redirect to recipe list after delete

    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})
def recipe_list(request):
	recipes = Recipe.objects.all()
	return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


@login_required
def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()

            # Update ingredients and directions separately
            ingredients = request.POST.getlist('ingredients')  # Assuming the name attribute for ingredients is 'ingredients'
            directions = request.POST.getlist('directions')  # Assuming the name attribute for directions is 'directions'

            # Update recipe's ingredients and directions
            recipe.ingredients = ingredients
            recipe.directions = directions
            recipe.save()

            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes/update_recipe.html', {'form': form, 'recipe': recipe})
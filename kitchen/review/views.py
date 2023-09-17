from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Review
from .forms import ReviewForm


def add_review(request, recipe_id):
	recipe = get_object_or_404(Recipe, pk=recipe_id)

	# Check if the user has already left a review for this recipe
	existing_review = Review.objects.filter(recipe=recipe, user=request.user).first()

	if existing_review:
		return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'existing_review': existing_review})

	if request.method == 'POST':
		form = ReviewForm(request.POST)

		if form.is_valid():
			review = form.save(commit=False)
			review.user = request.user
			review.recipe = recipe
			review.save()
			return redirect('recipe_detail', pk=recipe_id)
	else:
		form = ReviewForm()

	return render(request, 'recipes/../../templates/review/add_review.html', {'recipe': recipe, 'form': form})

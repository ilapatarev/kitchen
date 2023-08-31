from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.add_recipe, name='add_recipe'),
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
	path('recipes/', views.recipe_list, name='recipe_list'),
	path('update/<int:pk>/', views.update_recipe, name='update_recipe'),
]
from django.urls import path

from ProjectSoftUni.main_app.views.general import HomePageView, SearchView, AboutPageView

from ProjectSoftUni.main_app.views.recipe import \
    ShowRecipeView, CreateRecipeView, EditRecipeView, DeleteRecipeView, RecipesDashboardView

from ProjectSoftUni.main_app.views.product import \
    ShowProductView, CreateProductView, EditProductView, DeleteProductView, ProductsDashboardView

from ProjectSoftUni.main_app.views.course import \
    CreateCourseView, EditCourseView, DeleteCourseView, CoursesDashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home page'),

    path('recipe/add/', CreateRecipeView.as_view(), name='create recipe page'),
    path('recipe/dashboard', RecipesDashboardView.as_view(), name='recipe dashboard page'),
    path('recipe/<int:pk>/', ShowRecipeView.as_view(), name='show recipe page'),
    path('recipe/<int:pk>/edit/', EditRecipeView.as_view(), name='edit recipe page'),
    path('recipe/<int:pk>/delete/', DeleteRecipeView.as_view(), name='delete recipe page'),

    path('product/add/', CreateProductView.as_view(), name='create product page'),
    path('product/dashboard/', ProductsDashboardView.as_view(), name='product dashboard page'),
    path('product/<int:pk>/', ShowProductView.as_view(), name='show product page'),
    path('product/<int:pk>/edit/', EditProductView.as_view(), name='edit product page'),
    path('product/<int:pk>/delete/', DeleteProductView.as_view(), name='delete product page'),

    path('course/add/', CreateCourseView.as_view(), name='create course page'),
    path('course/dashboard/', CoursesDashboardView.as_view(), name='course dashboard page'),
    path('course/<int:pk>/edit/', EditCourseView.as_view(), name='edit course page'),
    path('course/<int:pk>/delete/', DeleteCourseView.as_view(), name='delete course page'),

    path('search/', SearchView.as_view(), name='search'),
    path('about/', AboutPageView.as_view(), name='about'),
]

import ProjectSoftUni.main_app.signals

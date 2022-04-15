from django.contrib import admin

# Register your models here.
from ProjectSoftUni.main_app.models import Recipe, Product, Course


@admin.register(Recipe)
class RecipesAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CoursesAdmin(admin.ModelAdmin):
    pass

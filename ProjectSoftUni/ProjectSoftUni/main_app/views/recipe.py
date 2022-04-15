from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from ProjectSoftUni.main_app.models import Recipe

from ProjectSoftUni.main_app.forms import CreateRecipeForm, EditRecipeForm

from ProjectSoftUni.common.custom_mixins import RecipeCustomMixin

from django.urls import reverse_lazy


class RecipesDashboardView(ListView):
    model = Recipe
    template_name = 'main/recipe/recipes_dashboard.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        # When a filter is selected.
        if self.request.GET.get('category'):
            query = self.request.GET.get('category')
            object_list = Recipe.objects.filter(category=query)

        else:
            object_list = Recipe.objects.all()

        return object_list

    # Get the selected category, so it can be shown in the template.
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['category'] = self.request.GET.get('category')
        return context


class ShowRecipeView(DetailView):
    model = Recipe
    template_name = 'main/recipe/show_recipe.html'
    context_object_name = 'recipe'


class CreateRecipeView(RecipeCustomMixin, CreateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'main/recipe/add_recipe.html'
    permission_required = 'main_app.add_recipe'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs

    # Go to the created recipe page.
    def get_success_url(self):
        return reverse_lazy('show recipe page', kwargs={'pk': self.object.pk})


class EditRecipeView(RecipeCustomMixin, UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    template_name = 'main/recipe/edit_recipe.html'
    permission_required = 'main_app.change_recipe'

    # Return to the same recipe page.
    def get_success_url(self):
        return reverse_lazy('show recipe page', kwargs={'pk': self.object.pk})


class DeleteRecipeView(RecipeCustomMixin, DeleteView):
    model = Recipe
    template_name = 'main/recipe/delete_recipe.html'
    permission_required = 'main_app.delete_recipe'

    # Return to user's recipes page.
    def get_success_url(self):
        return reverse_lazy('profile recipes page', kwargs={'pk': self.object.pk})

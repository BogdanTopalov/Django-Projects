from django.views.generic import DetailView, UpdateView, DeleteView, ListView

from ProjectSoftUni.accounts_app.models import Profile
from ProjectSoftUni.main_app.models import Recipe

from ProjectSoftUni.accounts_app.forms import UpdateProfileForm

from ProjectSoftUni.common.custom_mixins import UserPermissionMixin

from django.urls import reverse_lazy


class ShowProfileView(UserPermissionMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile/show_profile.html'
    context_object_name = 'profile'
    permission_required = 'accounts_app.view_profile'


class UpdateProfileView(UserPermissionMixin, UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'accounts/profile/edit_profile.html'
    permission_required = 'accounts_app.change_profile'

    def get_success_url(self):
        return reverse_lazy('show profile page', kwargs={'pk': self.object.pk})


class DeleteProfileView(UserPermissionMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile/delete_profile.html'
    success_url = reverse_lazy('register user page')
    permission_required = 'accounts_app.delete_profile'


class ProfileRecipesView(ListView):
    model = Recipe
    template_name = 'accounts/profile/profile_recipes.html'
    context_object_name = 'profile_recipes'
    ordering = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author_id=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        total_profile_recipes = len(self.object_list)
        context.update({
            'total_profile_recipes': total_profile_recipes,
        })
        return context

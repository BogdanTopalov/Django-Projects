from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect

from ProjectSoftUni.main_app.models import Recipe


class LoggedInMixin:
    def dispatch(self, request, *args, **kwargs):
        # When a logged user tries to access /login or /register from the URL.
        # Redirect to home page.
        if request.user.is_authenticated:
            return redirect('home page')

        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        # When user tries to view/edit/delete other profiles from the URL.
        # 403 Forbidden.
        if (not request.user.pk == kwargs['pk']) or (not self.has_permission()):
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class RecipeCustomMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # When user tries to edit/delete recipes which he isn't author of.
            # 403 Forbidden.
            if kwargs:
                recipe = Recipe.objects.get(pk=kwargs['pk'])
                if (not recipe.author == request.user) or (not self.has_permission()):
                    return self.handle_no_permission()

        if not request.user.is_authenticated:
            # When user tries to enter 'create recipe page' from the URL.
            # Redirect to login page.
            if request.path == '/recipe/add/':
                return redirect('login user page')

            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)


class StaffRequiredMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login user page')

        if not request.user.is_staff:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)

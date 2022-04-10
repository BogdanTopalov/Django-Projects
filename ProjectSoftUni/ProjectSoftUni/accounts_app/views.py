from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView

from ProjectSoftUni.accounts_app.forms import UserRegistrationForm, UserLoginForm, UpdateProfileForm
from ProjectSoftUni.accounts_app.models import Profile


class ShowProfileView(DetailView, PermissionRequiredMixin):
    template_name = 'accounts/profile.html'
    model = Profile

    # def dispatch(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)

    # permission_required = ('view_profile', 'view_accountscustomuser')
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if not self.has_permission():
    #         return self.handle_no_permission()
    #     return super().dispatch(request, *args, **kwargs)


class RegisterProfileView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home page')

    # Login user right after registration.
    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class LoginProfileView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('home page')


class LogoutProfileView(LogoutView):
    next_page = reverse_lazy('home page')


class UpdateProfileView(UpdateView):
    template_name = 'accounts/update.html'
    model = Profile
    # fields = ('email', 'first_name', 'last_name', 'picture')
    form_class = UpdateProfileForm

    def get_success_url(self):
        return reverse_lazy('show profile page', kwargs={'pk': self.object.pk})


class DeleteProfileView(DeleteView):
    template_name = 'accounts/delete.html'
    model = Profile
    success_url = reverse_lazy('register profile page')


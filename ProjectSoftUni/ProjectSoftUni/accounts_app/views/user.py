from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from ProjectSoftUni.accounts_app.forms import UserLoginForm, UserRegistrationForm

from ProjectSoftUni.common.custom_mixins import LoggedInMixin

from django.contrib.auth import login
from django.urls import reverse_lazy


class RegisterUserView(LoggedInMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/user/register.html'
    success_url = reverse_lazy('home page')

    # Login user right after registration.
    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class LoginUserView(LoggedInMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'accounts/user/login.html'

    def get_success_url(self):
        return reverse_lazy('home page')


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home page')


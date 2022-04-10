import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from ProjectSoftUni.accounts_app.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['autofocus'] = False

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

        self.fields['password2'].help_text = None
        self.fields['password1'].help_text = None

        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['autofocus'] = False

        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

        self.fields['username'].label = ''
        self.fields['password'].label = ''


class UpdateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email'].label = ''
        self.fields['date_of_birth'].label = 'Date Of Birth'

    class Meta:
        model = Profile
        fields = ('picture', 'first_name', 'last_name', 'email', 'date_of_birth')
        widgets = {
            'picture': forms.FileInput(),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': '1920-01-01',
                    'max': datetime.date.today()
                }
            ),
        }


from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from ProjectSoftUni.accounts_app.managers import AccountsManager

from django.core.validators import MinLengthValidator
from ProjectSoftUni.common.validators import only_letters_validator, MaxFileSizeInMbValidator


# Custom User model
class AccountsCustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AccountsManager()


UserModel = get_user_model()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    NAMES_MIN_LENGTH = 2
    MAX_PICTURE_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAMES_MIN_LENGTH),
            only_letters_validator
        ],
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=[
            MinLengthValidator(NAMES_MIN_LENGTH),
            only_letters_validator
        ],
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    picture = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
        validators=[
            MaxFileSizeInMbValidator(MAX_PICTURE_SIZE_IN_MB),
        ]
    )

    user = models.OneToOneField(
        AccountsCustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.email

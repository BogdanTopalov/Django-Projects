from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from ProjectSoftUni.accounts_app.models import Profile
from ProjectSoftUni.common.validators import MaxFileSizeInMbValidator

UserModel = get_user_model()


class Recipe(models.Model):
    MAX_TITLE_LENGTH = 50
    MIN_TITLE_LENGTH = 3
    MAX_DESCRIPTION_LENGTH = 500
    CHOICES = [
        (x, x)
        for x in
        ('Breakfast', 'Lunch', 'Dinner',
         'Snack', 'Appetizer', 'Dessert',
         'Soup', 'Salad', 'Drink')
    ]

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=[
            MinLengthValidator(MIN_TITLE_LENGTH)
        ]
    )

    image = models.ImageField(
        upload_to='recipes/',
        null=True,
        blank=True,
        validators=[
            MaxFileSizeInMbValidator(5),
        ],
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH
    )

    servings = models.PositiveIntegerField()

    category = models.CharField(
        max_length=30,
        choices=CHOICES,
    )

    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        # Make title lower for search optimization.
        self.title = self.title.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_INFO_LENGTH = 300

    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )

    price = models.PositiveIntegerField()

    info = models.TextField(
        max_length=MAX_INFO_LENGTH
    )

    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
        validators=[
            MaxFileSizeInMbValidator(5),
        ],
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    link = models.URLField()

    image = models.ImageField(
        upload_to='courses/',
        null=True,
        blank=True,
        validators=[
            MaxFileSizeInMbValidator(5),
        ],
    )

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

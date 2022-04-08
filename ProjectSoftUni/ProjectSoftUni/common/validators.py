from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# Validator for Profile model names
def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('The name must contain only letters!')


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_mb):
        self.max_mb = max_mb

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_mb * 1024 * 1024:
            raise ValidationError('The maximum file size is 5 MB.')

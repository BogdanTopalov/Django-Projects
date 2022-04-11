from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from ProjectSoftUni.accounts_app.models import AccountsCustomUser, Profile

UserModel = get_user_model()


# Save the user email in the Profile instance.
@receiver(post_save, sender=UserModel)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            email=instance.email
        )


# Update user instance email if the Profile email is changed.
@receiver(post_save, sender=Profile)
def update_profile(instance, **kwargs):
    if not instance.user.email == instance.email:
        instance.user.email = instance.email
        instance.user.save()


# Delete the user instance after the Profile one.
@receiver(post_delete, sender=Profile)
def delete_profile(instance, **kwargs):
    # Delete the profile picture.
    if instance.picture:
        instance.picture.delete()
    instance.user.delete()

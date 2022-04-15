from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from ProjectSoftUni.accounts_app.models import Profile

UserModel = get_user_model()


# Save the user email in the Profile instance.
# and give the user a permission group.
@receiver(post_save, sender=UserModel)
def create_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            email=instance.email
        )
    regular_user_group = Group.objects.get(name='RegularUser')
    instance.groups.add(regular_user_group)


# Update user auth email if the Profile email is changed.
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


# Delete old picture when profile picture is changed.
@receiver(pre_save, sender=Profile)
def profile_picture_change(instance, *args, **kwargs):
    if instance.picture:
        try:
            try:
                old_picture = Profile.objects.get(pk=instance.pk).picture.path
            except ValueError:
                old_picture = ''
            try:
                new_picture = instance.picture.path
            except():
                new_picture = None
            if new_picture != old_picture:
                import os
                if os.path.exists(old_picture):
                    os.remove(old_picture)
        except():
            pass

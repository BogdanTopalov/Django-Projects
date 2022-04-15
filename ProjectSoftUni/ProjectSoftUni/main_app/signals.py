from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from ProjectSoftUni.main_app.models import Recipe, Product, Course


# Delete image before the instance is deleted.
@receiver(pre_delete, sender=Recipe)
@receiver(pre_delete, sender=Product)
@receiver(pre_delete, sender=Course)
def delete_image(instance, **kwargs):
    instance.image.delete()


# Delete old image when instance image is updated.
@receiver(pre_save, sender=Recipe)
@receiver(pre_save, sender=Product)
@receiver(pre_save, sender=Course)
def pre_save_image_change(instance, *args, **kwargs):
    if instance.pk and instance.image:
        try:
            old_image = instance.__class__.objects.get(pk=instance.pk).image.path
            try:
                new_image = instance.image.path
            except():
                new_image = None
            if new_image != old_image:
                import os
                if os.path.exists(old_image):
                    os.remove(old_image)
        except():
            pass

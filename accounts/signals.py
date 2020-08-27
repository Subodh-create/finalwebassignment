from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . import models

@receiver(post_save,sender=User)
def create_profile(sender=User, instance=None, created=False, *args, **kwargs):
    if created:
        if instance.is_superuser:
            prof = models.Profile(
                utype = "NU", user = instance   
            )
            prof.save()
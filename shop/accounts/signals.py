
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, ProfileUser


@receiver(post_save, sender=User)
def creat_profile(sender, **kwargs):
    if kwargs['created']:
        ProfileUser.objects.create(user=kwargs['instance'])

# post_save.connect(receiver=creat_profile, sender=User)

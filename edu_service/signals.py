from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

'''
# На случай важных переговоров.
# А если серьёзно, то если понадобится расширить модель User
# своими полями, то здесь идет перехват сигнала создания базового пользователя, чтобы одновременно создать 
# расширенную модель для этого же пользователя. 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
'''
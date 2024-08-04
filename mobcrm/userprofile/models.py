from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=50, choices=[
        ('Base Mobilizer', 'Base Mobilizer'),
        ('Regional Mobilizer', 'Regional Mobilizer'),
        ('Golbal Team', 'Global Team'),
        ('Mobilization Director', 'Mobilization Director'),
        ('Office Executive Director', 'Office Executive Director'),
        ('Other', 'Other'),
    ])

    def __str__(self):
        return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

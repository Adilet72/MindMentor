from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from .models import *

@receiver(post_migrate)
def load_data(sender, **kwargs):
    if not Specialization.objects.exists() and not Experience.objects.exists():
        call_command('loaddata', 'apps/users/fixtures/specialization_experience_fixtures.json')
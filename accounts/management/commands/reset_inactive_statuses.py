from django.core.management.base import BaseCommand
from django.utils import timezone
from django.db.models import F
from accounts.models import UserRegistrationForm

class Command(BaseCommand):
    help = 'Reset user active statuses based on elapsed time.'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        users_to_reset = UserRegistrationForm.objects.filter(
            is_publish=True,
            status_set_at__isnull=False,
            status_set_at__lte=now - F('status_duration')
        )

        for user in users_to_reset:
            user.deactivate()

        self.stdout.write(self.style.SUCCESS('Successfully reset inactive statuses.'))
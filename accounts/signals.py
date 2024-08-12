from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import User, UserRegistrationForm

@receiver(post_save, sender=UserRegistrationForm)
def send_activation_email(sender, instance, **kwargs):
    if instance.tracker.has_changed('is_publish') and instance.is_publish:
        send_mail(
            'Account Activated',
            '''Dear Sir/Madam,
            Your account has been activated.
            ''',
            settings.DEFAULT_FROM_EMAIL,
            [instance.user.email],
            fail_silently=False,
        )

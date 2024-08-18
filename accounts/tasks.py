from celery import shared_task
from .views import auto_deactivate_users

@shared_task
def auto_deactivate_users_task():
    auto_deactivate_users()
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'khulna_university.settings')

app = Celery('khulna_university')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     from django_celery_beat.models import PeriodicTask, IntervalSchedule
#     from datetime import timedelta
#     schedule, created = IntervalSchedule.objects.get_or_create(
#         every=10,
#         period=IntervalSchedule.MINUTES,
#         #period=IntervalSchedule.HOURS,
#     )
#     PeriodicTask.objects.get_or_create(
#         interval=schedule,
#         name='Reset inactive statuses',
#         task='accounts.tasks.auto_deactivate_users_task',
#     )
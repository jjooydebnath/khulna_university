from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'khulna_university.settings')
app = Celery('accounts')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from django_celery_beat.models import PeriodicTask, IntervalSchedule
    from datetime import timedelta
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.HOURS,
    )
    PeriodicTask.objects.get_or_create(
        interval=schedule,
        name='Reset inactive statuses',
        task='accounts.tasks.reset_inactive_statuses_task',
    )
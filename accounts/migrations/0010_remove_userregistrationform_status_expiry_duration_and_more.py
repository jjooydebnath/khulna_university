# Generated by Django 5.0.8 on 2024-08-13 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_userregistrationform_status_expiry_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistrationform',
            name='status_expiry_duration',
        ),
        migrations.RemoveField(
            model_name='userregistrationform',
            name='status_set_at',
        ),
    ]

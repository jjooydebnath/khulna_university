# Generated by Django 5.1 on 2024-08-13 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userregistrationform_end_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistrationform',
            old_name='end_time',
            new_name='active_since',
        ),
    ]

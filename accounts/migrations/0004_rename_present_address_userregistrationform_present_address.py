# Generated by Django 5.0.7 on 2024-07-28 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userregistrationform_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistrationform',
            old_name='Present_address',
            new_name='present_address',
        ),
    ]

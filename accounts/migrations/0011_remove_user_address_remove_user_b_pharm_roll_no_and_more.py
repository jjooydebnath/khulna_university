# Generated by Django 5.0.7 on 2024-08-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_adminregister_is_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='b_pharm_roll_no',
        ),
        migrations.RemoveField(
            model_name='user',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='designation_and_department',
        ),
        migrations.RemoveField(
            model_name='user',
            name='hobbies',
        ),
        migrations.RemoveField(
            model_name='user',
            name='m_pharm_roll_no',
        ),
        migrations.RemoveField(
            model_name='user',
            name='marriage_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name_of_spouse',
        ),
        migrations.RemoveField(
            model_name='user',
            name='no_of_kids',
        ),
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='user',
            name='permanent_address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='present_address',
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='b_pharm_roll_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='blood_group',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='designation_and_department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='hobbies',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='m_pharm_roll_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='marriage_date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='name_of_spouse',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='no_of_kids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='organization',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='permanent_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userregistrationform',
            name='present_address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]

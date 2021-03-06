# Generated by Django 2.2.13 on 2021-02-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_remove_user_account_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='requested_role',
            field=models.CharField(choices=[('subscriber', 'Subscriber'), ('student', 'Student'), ('teacher', 'Teacher'), ('editor', 'Editor'), ('academic_officer', 'Academic Officer'), ('admin', 'Admin')], default='subscriber', max_length=50),
        ),
    ]

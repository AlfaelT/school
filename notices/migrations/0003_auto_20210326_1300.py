# Generated by Django 2.2.13 on 2021-03-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_notice_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='expires_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]

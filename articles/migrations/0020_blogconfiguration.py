# Generated by Django 2.2.13 on 2021-03-24 19:41

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_newsletter_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('theme_name', models.CharField(max_length=50)),
                ('theme_preview', models.ImageField(upload_to='blogtheme/previews/')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]

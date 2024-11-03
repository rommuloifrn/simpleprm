# Generated by Django 5.1.2 on 2024-11-03 04:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contact_birthday_alter_contact_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_time_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
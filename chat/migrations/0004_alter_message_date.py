# Generated by Django 5.0.4 on 2024-04-04 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 4, 19, 39, 22, 535071)),
        ),
    ]

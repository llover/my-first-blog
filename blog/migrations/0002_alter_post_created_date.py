# Generated by Django 4.0.3 on 2022-09-24 09:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 9, 22, 52, 75858, tzinfo=utc)),
        ),
    ]

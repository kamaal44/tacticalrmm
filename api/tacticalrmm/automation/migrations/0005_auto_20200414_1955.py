# Generated by Django 3.0.5 on 2020-04-14 19:55

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_auto_20200411_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automatedtask',
            name='run_time_days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], null=True), blank=True, default=list, null=True, size=None),
        ),
    ]
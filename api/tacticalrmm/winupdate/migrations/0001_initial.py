# Generated by Django 3.0.6 on 2020-05-31 01:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WinUpdatePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critical', models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore')], default='manual', max_length=100)),
                ('important', models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore')], default='manual', max_length=100)),
                ('moderate', models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore')], default='manual', max_length=100)),
                ('low', models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore')], default='manual', max_length=100)),
                ('other', models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore')], default='manual', max_length=100)),
                ('run_time_hour', models.IntegerField(choices=[(0, '12 AM'), (1, '01 AM'), (2, '02 AM'), (3, '03 AM'), (4, '04 AM'), (5, '05 AM'), (6, '06 AM'), (7, '07 AM'), (8, '08 AM'), (9, '09 AM'), (10, '10 AM'), (11, '11 AM'), (12, '12 PM'), (13, '01 PM'), (14, '02 PM'), (15, '03 PM'), (16, '04 PM'), (17, '05 PM'), (18, '06 PM'), (19, '07 PM'), (20, '08 PM'), (21, '09 PM'), (22, '10 PM'), (23, '11 PM')], default=3)),
                ('run_time_days', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), blank=True, default=list, null=True, size=None)),
                ('reboot_after_install', models.CharField(choices=[('never', 'Never'), ('required', 'When Required'), ('always', 'Always')], default='required', max_length=50)),
                ('reprocess_failed', models.BooleanField(default=False)),
                ('reprocess_failed_times', models.PositiveIntegerField(default=5)),
                ('email_if_fail', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winupdatepolicy', to='agents.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='WinUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(max_length=255, null=True)),
                ('kb', models.CharField(max_length=100, null=True)),
                ('mandatory', models.BooleanField(default=False)),
                ('title', models.TextField(null=True)),
                ('needs_reboot', models.BooleanField(default=False)),
                ('installed', models.BooleanField(default=False)),
                ('downloaded', models.BooleanField(default=False)),
                ('description', models.TextField(null=True)),
                ('severity', models.CharField(blank=True, max_length=255, null=True)),
                ('action', models.CharField(choices=[('inherit', 'Inherit'), ('approve', 'Approve'), ('ignore', 'Ignore'), ('nothing', 'Do Nothing')], default='nothing', max_length=100)),
                ('result', models.CharField(default='n/a', max_length=255)),
                ('date_installed', models.DateTimeField(null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winupdates', to='agents.Agent')),
            ],
        ),
    ]

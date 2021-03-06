# Generated by Django 3.0.6 on 2020-05-31 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('filename', models.CharField(max_length=255)),
                ('shell', models.CharField(choices=[('powershell', 'Powershell'), ('cmd', 'Batch (CMD)'), ('python', 'Python')], default='powershell', max_length=100)),
            ],
        ),
    ]

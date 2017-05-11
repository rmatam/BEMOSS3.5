# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationRegistered',
            fields=[
                ('application', models.AutoField(primary_key=True, serialize=False)),
                ('app_name', models.CharField(blank=True, max_length=50, null=True)),
                ('executable', models.CharField(blank=True, max_length=50, null=True)),
                ('auth_token', models.CharField(blank=True, max_length=50, null=True)),
                ('app_user', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('registered_time', models.DateTimeField()),
                ('last_updated_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'application_registered',
            },
        ),
        migrations.CreateModel(
            name='ApplicationRunning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('app_settings', models.CharField(blank=True, max_length=200, null=True)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bemoss_applications.ApplicationRegistered')),
            ],
            options={
                'db_table': 'application_running',
            },
        ),
    ]

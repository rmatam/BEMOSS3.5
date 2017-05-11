# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-13 16:08
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_paramter', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('created_on', models.DateTimeField()),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'alerts',
            },
        ),
        migrations.CreateModel(
            name='AlertTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_description', models.CharField(max_length=50)),
                ('alert_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'alert_types',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('dt_triggered', models.DateTimeField()),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'notification',
            },
        ),
        migrations.CreateModel(
            name='NotificationChannelAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'alerts_notificationchanneladdress',
            },
        ),
        migrations.CreateModel(
            name='NotificationChannels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_channel', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'notification_channel',
            },
        ),
        migrations.CreateModel(
            name='PossibleEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'possible_events',
            },
        ),
        migrations.CreateModel(
            name='PriorityLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_level', models.CharField(max_length=20)),
                ('priority_notification_hours', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'priority',
            },
        ),
        migrations.AddField(
            model_name='notificationchanneladdresses',
            name='notification_channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.NotificationChannels'),
        ),
        migrations.AddField(
            model_name='notification',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.PossibleEvents'),
        ),
        migrations.AddField(
            model_name='alerttypes',
            name='associated_events',
            field=models.ManyToManyField(to='alerts.PossibleEvents'),
        ),
        migrations.AddField(
            model_name='alerts',
            name='alert_channels',
            field=models.ManyToManyField(to='alerts.NotificationChannelAddresses'),
        ),
        migrations.AddField(
            model_name='alerts',
            name='alert_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.AlertTypes'),
        ),
        migrations.AddField(
            model_name='alerts',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.PriorityLevels'),
        ),
        migrations.AddField(
            model_name='alerts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
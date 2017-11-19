# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zoxon470GitLabProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=125, verbose_name='Логин от GitLab')),
                ('commits_per_day', models.IntegerField(verbose_name='Комиты за день')),
                ('commits_per_week', models.IntegerField(verbose_name='Комиты за неделю')),
                ('commits_per_month', models.IntegerField(verbose_name='Комиты за месяц')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-02-26 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-10 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FizzBuzz',
            fields=[
                ('fizzbuzz_id', models.AutoField(primary_key=True, serialize=False)),
                ('useragent', models.CharField(blank=True, max_length=500)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]

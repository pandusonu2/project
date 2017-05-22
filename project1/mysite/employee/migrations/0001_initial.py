# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=250)),
                ('emp_age', models.CharField(max_length=50)),
                ('emp_gender', models.CharField(max_length=10)),
                ('emp_desig', models.CharField(max_length=100)),
            ],
        ),
    ]

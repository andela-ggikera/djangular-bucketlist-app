# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_auto_20160204_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlistitem',
            name='bucketlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Bucketlist'),
        ),
    ]

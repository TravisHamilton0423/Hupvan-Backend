# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-10-11 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211009_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Driver'),
        ),
        migrations.AlterField(
            model_name='book',
            name='partner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Partner'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-10-13 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20211012_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('rating', models.FloatField(verbose_name='raiting')),
                ('image', models.FileField(upload_to='uploads/storage/')),
            ],
        ),
        migrations.CreateModel(
            name='StoreHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('image', models.FileField(upload_to='uploads/storehouse/')),
                ('size', models.IntegerField(verbose_name='Size')),
                ('time', models.IntegerField(verbose_name='Time')),
                ('cost', models.IntegerField(verbose_name='Cost')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storehouses', to='api.Storage')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='partner',
        ),
        migrations.AddField(
            model_name='homeofficestuff',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Storage'),
        ),
    ]
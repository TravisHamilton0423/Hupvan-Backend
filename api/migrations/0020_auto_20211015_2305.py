# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-10-15 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20211015_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='category',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='colour',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Colour'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='current_address',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Current address'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='currently_drive_for_other',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Currently drive for other'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='disability',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Disability'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driving_category',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Driving category'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='ethnicity',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Ethnicity'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='gender',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='has_license',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Has license'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='insurance_policy',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Insurance policy'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='license_plate_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='License plate number'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='national_insurance_number',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='National insurance number'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='own_car',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Own car'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='post_code',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Post code'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='proficiency',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Proficiency'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='seater',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Seater'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='street_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Street name'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='taxi_license',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Taxi license'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='vehicle_model',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Vehicle model'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='vehicle_type',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Vehicle type'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='year',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Year'),
        ),
    ]

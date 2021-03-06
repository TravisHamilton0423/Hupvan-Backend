# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2021-10-09 00:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('home', 'Home'), ('office', 'Office'), ('stuff', 'Stuff'), ('rubbish', 'Rubbish'), ('skip_hire', 'Skip hire'), ('storage', 'Storage')], default='home', max_length=15, verbose_name='Type')),
                ('state', models.CharField(choices=[('waiting', 'Waiting'), ('in_progress', 'In progress'), ('completed', 'Completed')], default='home', max_length=15, verbose_name='State')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('verification_code', models.CharField(max_length=10, verbose_name='Verification code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('approved_state', models.BooleanField(default=False, verbose_name='Approve')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HomeOfficeStuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_address', models.CharField(max_length=100, verbose_name='Pickup address')),
                ('destination_address', models.CharField(max_length=100, verbose_name='Destination address')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('floor', models.IntegerField(verbose_name='Floor')),
                ('number_of_rooms', models.IntegerField(verbose_name='Number of rooms')),
                ('lift', models.BooleanField(verbose_name='Is there a lift')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='homeofficestuff', to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('industry', models.CharField(max_length=100, verbose_name='Industry')),
                ('telephone', models.CharField(max_length=20, verbose_name='Telephone')),
                ('business_email', models.EmailField(default='partner@test.com', max_length=20, verbose_name='Business email')),
                ('website', models.CharField(max_length=30, verbose_name='Website')),
                ('short_bio', models.TextField(verbose_name='Short bio')),
                ('type', models.CharField(choices=[('storage', 'Storage'), ('van_hire', 'Van hire'), ('equipment_hire', 'Equipment hire'), ('other', 'Other')], default='storage', max_length=15, verbose_name='Type')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='partner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='Url')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('customer', 'Customer'), ('driver', 'Driver'), ('partner', 'Partner')], default='customer', max_length=15, verbose_name='Role')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='role', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rubbish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_address', models.CharField(max_length=100, verbose_name='Pickup address')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rubbish', to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='VanHire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_address', models.CharField(max_length=100, verbose_name='Pickup address')),
                ('from_datetime', models.DateTimeField(verbose_name='From')),
                ('until_datetime', models.DateTimeField(verbose_name='Until')),
                ('type_of_waste', models.CharField(choices=[('general', 'General'), ('plasterboard', 'Plasterboard')], default='home', max_length=15, verbose_name='Type of waste')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='van_hire', to='api.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Customer'),
        ),
        migrations.AddField(
            model_name='book',
            name='driver',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Driver'),
        ),
        migrations.AddField(
            model_name='book',
            name='partner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Partner'),
        ),
    ]

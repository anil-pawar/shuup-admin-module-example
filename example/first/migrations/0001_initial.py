# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-07-07 15:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup', '0060_supplier_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=200, unique=True, verbose_name='Unique Identifier')),
                ('first_name', models.CharField(max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, verbose_name='Last Name')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='modified at')),
                ('modified_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_shop', to='shuup.Shop', verbose_name='shop')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-10 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20161010_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='recipe_groups.Cuisine', verbose_name='cuisine'),
            preserve_default=False,
        ),
    ]
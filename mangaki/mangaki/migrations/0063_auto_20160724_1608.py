# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-24 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0062_tag_nb_works_linked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.TextField(unique=True),
        ),
    ]
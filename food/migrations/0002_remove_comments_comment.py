# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-05 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment',
        ),
    ]
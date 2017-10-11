# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0007_dlda_oopm'),
    ]

    operations = [
        migrations.AddField(
            model_name='am3',
            name='res1',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='am3',
            name='res2',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res1',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res2',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res1',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res2',
            field=models.IntegerField(default=3),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antiques', '0005_type_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='shippable',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='type',
            name='type_thumbnail',
            field=models.FileField(default='None', upload_to=b''),
            preserve_default=False,
        ),
    ]

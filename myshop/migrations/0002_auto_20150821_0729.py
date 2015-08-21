# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legacy_redirect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='legacylink',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
            preserve_default=True,
        ),
    ]

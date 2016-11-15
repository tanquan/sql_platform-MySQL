# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0014_auto_20161029_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_account',
            name='instance',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='db_name',
            name='instance',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

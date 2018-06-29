# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-05-11 19:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='caritem',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='caritem',
            unique_together=set([('cart_key', 'product')]),
        ),
    ]
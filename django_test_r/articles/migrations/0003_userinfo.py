# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-18 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(max_length=25)),
                ('username', models.TextField(max_length=254)),
                ('password', models.TextField(max_length=25)),
                ('role', models.TextField(max_length=50)),
                ('certification', models.TextField(max_length=25)),
                ('specialization', models.TextField(max_length=50)),
                ('hward', models.TextField(max_length=25)),
            ],
        ),
    ]

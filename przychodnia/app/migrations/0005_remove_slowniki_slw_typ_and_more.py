# Generated by Django 4.1 on 2023-12-09 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_kntkarty_knt_create_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slowniki',
            name='slw_typ',
        ),
        migrations.AlterField(
            model_name='kntkarty',
            name='knt_create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 11, 58, 6, 158624)),
        ),
        migrations.AlterField(
            model_name='kntkarty',
            name='knt_lastmod_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 9, 11, 58, 6, 158624)),
        ),
    ]
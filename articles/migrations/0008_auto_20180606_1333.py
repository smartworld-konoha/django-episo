# Generated by Django 2.0.5 on 2018-06-06 13:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20180606_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-04 08:54

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0005_auto_20180604_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='free_links',
            field=jsonfield.fields.JSONField(blank=True, default=[], null=True, verbose_name='free_links'),
        ),
    ]

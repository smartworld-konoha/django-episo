# Generated by Django 2.0.5 on 2018-06-04 08:49

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0003_auto_20180604_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='free_links',
            field=jsonfield.fields.JSONField(blank=True, null=True, verbose_name='free_links'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-06-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0008_auto_20180606_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name_slug',
            field=models.SlugField(blank=True, default='', null=True, unique=True),
        ),
    ]
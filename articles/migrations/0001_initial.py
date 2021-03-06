# Generated by Django 2.0.5 on 2018-06-03 02:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('is_featured', models.BooleanField(default=False)),
                ('cover_image', models.FileField(default='default.png', upload_to='uploads/')),
                ('member_name', models.TextField(blank=True, null=True)),
                ('member_title', models.TextField(blank=True, null=True)),
                ('attribute', models.TextField(blank=True, null=True)),
                ('region', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('free_links', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='free_links')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('brand', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='brands.Brand')),
            ],
        ),
    ]

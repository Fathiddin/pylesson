# Generated by Django 4.1.1 on 2022-10-29 06:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

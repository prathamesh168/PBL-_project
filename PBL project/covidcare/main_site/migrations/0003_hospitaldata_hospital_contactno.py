# Generated by Django 3.2.5 on 2021-07-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_auto_20210704_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitaldata',
            name='Hospital_ContactNo',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]

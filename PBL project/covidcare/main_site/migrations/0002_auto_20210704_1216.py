# Generated by Django 3.2.5 on 2021-07-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitaldata',
            name='Hospital_ICUBeds',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitaldata',
            name='Hospital_Pincode',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]

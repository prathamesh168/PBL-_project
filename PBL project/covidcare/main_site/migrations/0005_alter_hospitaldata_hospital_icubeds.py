# Generated by Django 3.2.5 on 2021-07-04 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_alter_hospitaldata_hospital_icubeds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitaldata',
            name='Hospital_ICUBeds',
            field=models.BooleanField(),
        ),
    ]

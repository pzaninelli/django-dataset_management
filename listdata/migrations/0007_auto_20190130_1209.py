# Generated by Django 2.1.5 on 2019-01-30 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listdata', '0006_auto_20190130_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='EndPeriod',
            field=models.DateTimeField(default='9999-12-31'),
        ),
        migrations.AlterField(
            model_name='filedata',
            name='StartPeriod',
            field=models.DateTimeField(default='9999-12-31'),
        ),
    ]

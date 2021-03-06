# Generated by Django 2.1.5 on 2019-01-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listdata', '0003_auto_20190130_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vartype',
            name='GCMName',
            field=models.CharField(blank=True, help_text='Global Climate Model name', max_length=20),
        ),
        migrations.AlterField(
            model_name='vartype',
            name='RCMName',
            field=models.CharField(blank=True, help_text='Regional Climate Model name', max_length=20),
        ),
    ]

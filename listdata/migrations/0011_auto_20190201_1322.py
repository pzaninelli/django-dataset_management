# Generated by Django 2.1.5 on 2019-02-01 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listdata', '0010_auto_20190201_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datainstance',
            name='filedata',
        ),
        migrations.AlterField(
            model_name='filedata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='DataInstance',
        ),
    ]

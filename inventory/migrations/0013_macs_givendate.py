# Generated by Django 2.1.5 on 2020-08-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20200810_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='macs',
            name='givenDate',
            field=models.CharField(default='', max_length=50, verbose_name='Given Date'),
        ),
    ]

# Generated by Django 2.1.5 on 2020-08-12 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_auto_20200811_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peripherals',
            name='givenDate',
            field=models.CharField(default='2000-1-1', max_length=50, verbose_name='Given Date'),
        ),
    ]
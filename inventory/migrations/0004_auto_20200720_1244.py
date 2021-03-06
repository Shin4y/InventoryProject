# Generated by Django 2.1.5 on 2020-07-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200714_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonobject',
            name='location',
            field=models.CharField(default='', max_length=50, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='commonobject',
            name='locationType',
            field=models.CharField(choices=[('WWH', 'WWH'), ('60FifthAve', '60FifthAve'), ('Other', 'Other')], default='', max_length=50, verbose_name='Location Type'),
        ),
        migrations.AlterField(
            model_name='commonobject',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='datacenterequipment',
            name='Type',
            field=models.CharField(default='', max_length=50, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='desktops',
            name='user',
            field=models.CharField(default='', max_length=50, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='make',
            field=models.CharField(max_length=50, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='purpose',
            field=models.CharField(default='', max_length=50, verbose_name='Purpose'),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='size',
            field=models.CharField(default='', max_length=50, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='notebooks',
            name='user',
            field=models.CharField(default='', max_length=50, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='stationaryprojectors',
            name='bulb',
            field=models.CharField(max_length=50, verbose_name='Bulb'),
        ),
    ]

# Generated by Django 2.1.5 on 2020-07-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacenterequipment',
            name='slug',
            field=models.SlugField(default='dataCenterEquipment'),
        ),
        migrations.AddField(
            model_name='desktops',
            name='slug',
            field=models.SlugField(default='desktop'),
        ),
        migrations.AddField(
            model_name='desktopscanners',
            name='slug',
            field=models.SlugField(default='desktopScanner'),
        ),
        migrations.AddField(
            model_name='notebooks',
            name='slug',
            field=models.SlugField(default='notebook'),
        ),
        migrations.AddField(
            model_name='peripherals',
            name='slug',
            field=models.SlugField(default='peripheral'),
        ),
        migrations.AddField(
            model_name='printers',
            name='slug',
            field=models.SlugField(default='printer'),
        ),
        migrations.AddField(
            model_name='stationaryprojectors',
            name='slug',
            field=models.SlugField(default='stationaryProjector'),
        ),
    ]
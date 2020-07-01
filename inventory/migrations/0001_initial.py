# Generated by Django 2.1.5 on 2020-06-29 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataCenterEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
                ('modelName', models.CharField(max_length=50)),
                ('macAddress', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('serialNumber', models.CharField(max_length=50)),
                ('assetTag', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Desktops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
                ('modelName', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('serialNumber', models.CharField(max_length=50)),
                ('macAddress', models.CharField(max_length=50)),
                ('IPAddress', models.CharField(max_length=50)),
                ('OS', models.CharField(max_length=50)),
                ('userType', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DesktopScanners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
                ('modelName', models.CharField(max_length=50)),
                ('serialNumber', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
                ('modelName', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('modelNumber', models.CharField(max_length=50)),
                ('OS', models.CharField(max_length=50)),
                ('serialNumber', models.CharField(max_length=50)),
                ('manufacturedYear', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=50)),
                ('userType', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Peripherals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
                ('modelName', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('make', models.CharField(max_length=50)),
                ('givenDate', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Printers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
                ('modelName', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('cartridgeType', models.CharField(max_length=50)),
                ('macAddress', models.CharField(max_length=50)),
                ('givenDate', models.CharField(max_length=50)),
                ('serialNumber', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StationaryProjectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=100)),
                ('modelName', models.CharField(max_length=50)),
                ('bulb', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
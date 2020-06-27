# Generated by Django 2.1.5 on 2020-06-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
                ('locationType', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('dateLastModified', models.DateTimeField(editable=False)),
                ('serialNumber', models.CharField(max_length=50)),
                ('macAddress', models.CharField(max_length=50)),
                ('IPAddress', models.CharField(max_length=50)),
                ('OS', models.CharField(max_length=50)),
                ('userType', models.CharField(max_length=50)),
                ('Notes', models.CharField(max_length=50)),
                ('lastUpdatedUser', models.CharField(max_length=50)),
            ],
        ),
    ]

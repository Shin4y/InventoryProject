# Generated by Django 2.1.5 on 2020-07-24 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20200722_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commonobject',
            old_name='location',
            new_name='room',
        ),
    ]
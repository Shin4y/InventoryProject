# Generated by Django 2.1.5 on 2020-08-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20200806_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonobject',
            name='Notes',
            field=models.CharField(max_length=500),
        ),
    ]
# Generated by Django 2.1.5 on 2020-07-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_commonobject_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonobject',
            name='room',
            field=models.CharField(default='', max_length=50, verbose_name='Room'),
        ),
    ]

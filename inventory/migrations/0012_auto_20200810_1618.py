# Generated by Django 2.1.5 on 2020-08-10 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_auto_20200806_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Macs',
            fields=[
                ('commonobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.commonObject')),
                ('serialNumber', models.CharField(default='', max_length=50, verbose_name='Serial Number')),
                ('partNumber', models.CharField(default='', max_length=50, verbose_name='Part Number')),
                ('modelNumber', models.CharField(default='', max_length=50, verbose_name='Model Number')),
                ('size', models.CharField(default='', max_length=50, verbose_name='Size')),
                ('manufactureYear', models.CharField(default='', max_length=50, verbose_name='Manufactured Year')),
                ('appleCareNumber', models.CharField(default='', max_length=50, verbose_name='AppleCare Registration Number')),
                ('designation', models.CharField(default='', max_length=50, verbose_name='Designation')),
                ('user', models.CharField(default='', max_length=50, verbose_name='Given To')),
                ('userType', models.CharField(default='', max_length=50, verbose_name='User Type')),
                ('purchaseDate', models.CharField(default='', max_length=50, verbose_name='Purchase Date')),
                ('purpose', models.CharField(default='', max_length=50, verbose_name='Purpose')),
            ],
            bases=('inventory.commonobject',),
        ),
        migrations.AlterField(
            model_name='commonobject',
            name='Notes',
            field=models.CharField(max_length=200),
        ),
    ]

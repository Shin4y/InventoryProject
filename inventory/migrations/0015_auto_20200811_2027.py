# Generated by Django 2.1.5 on 2020-08-12 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_macs_applecareexpirationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonobject',
            name='modelName',
            field=models.CharField(default='', max_length=255, verbose_name='Model Name'),
        ),
        migrations.AlterField(
            model_name='commonobject',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='commonobject',
            name='token',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='desktops',
            name='macAddress',
            field=models.CharField(default='', max_length=255, verbose_name='Mac Address'),
        ),
        migrations.AlterField(
            model_name='desktops',
            name='serialNumber',
            field=models.CharField(default='', max_length=255, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='appleCareExpirationDate',
            field=models.CharField(default='', max_length=255, verbose_name='AppleCare Expiration Date'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='appleCareNumber',
            field=models.CharField(default='', max_length=255, verbose_name='AppleCare Registration Number'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='designation',
            field=models.CharField(default='', max_length=255, verbose_name='Designation'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='givenDate',
            field=models.CharField(default='', max_length=255, verbose_name='Given Date'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='manufactureYear',
            field=models.CharField(default='', max_length=255, verbose_name='Manufactured Year'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='modelNumber',
            field=models.CharField(default='', max_length=255, verbose_name='Model Number'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='partNumber',
            field=models.CharField(default='', max_length=255, verbose_name='Part Number'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='purchaseDate',
            field=models.CharField(default='', max_length=255, verbose_name='Purchase Date'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='purpose',
            field=models.CharField(default='', max_length=255, verbose_name='Purpose'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='serialNumber',
            field=models.CharField(default='', max_length=255, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='size',
            field=models.CharField(default='', max_length=255, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='user',
            field=models.CharField(default='', max_length=255, verbose_name='Given To'),
        ),
        migrations.AlterField(
            model_name='macs',
            name='userType',
            field=models.CharField(default='', max_length=255, verbose_name='User Type'),
        ),
    ]

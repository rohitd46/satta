# Generated by Django 4.1 on 2022-08-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satta_king', '0008_managebank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managebank',
            name='GooglePayNumber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='managebank',
            name='PayTmNUmber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='managebank',
            name='PhonePayNumber',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 4.1 on 2022-10-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satta_king', '0022_galidisawartime_starlinetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailytime',
            name='Close_Time',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='dailytime',
            name='Opne_Time',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='galidisawartime',
            name='Open_Time',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='starlinetime',
            name='Open_Time',
            field=models.CharField(max_length=5),
        ),
    ]

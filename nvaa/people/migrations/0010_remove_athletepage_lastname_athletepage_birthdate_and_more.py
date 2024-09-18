# Generated by Django 5.0.9 on 2024-09-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_athletepage_teampage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athletepage',
            name='lastname',
        ),
        migrations.AddField(
            model_name='athletepage',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Geburtstag'),
        ),
        migrations.AddField(
            model_name='athletepage',
            name='sports',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sportarten'),
        ),
        migrations.AddField(
            model_name='athletepage',
            name='teaser',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Teaser'),
        ),
        migrations.AddField(
            model_name='teampage',
            name='sports',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sportarten'),
        ),
        migrations.AlterField(
            model_name='teampage',
            name='teaser',
            field=models.TextField(blank=True, max_length=256, null=True, verbose_name='Teaser'),
        ),
    ]

# Generated by Django 5.0.9 on 2024-09-20 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='value',
        ),
    ]

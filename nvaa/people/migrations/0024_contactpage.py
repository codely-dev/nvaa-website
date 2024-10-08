# Generated by Django 5.0.9 on 2024-09-19 16:59

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0023_remove_athletesindexpage_bio_brandpage_bio'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0026_delete_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('teaser', models.TextField(blank=True, max_length=256, null=True, verbose_name='Teaser')),
                ('bio', wagtail.fields.StreamField([('paragraph', 0)], blank=True, block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {})}, null=True)),
                ('portrait', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontakt',
            },
            bases=('wagtailcore.page',),
        ),
    ]

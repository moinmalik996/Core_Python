# Generated by Django 4.0.4 on 2022-05-12 17:11

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('Title_And_Text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add Title', max_length=100, required=True)), ('subtitle', wagtail.core.blocks.TextBlock(help_text='Add Subtitle', max_length=100, required=True))]))], blank=True, null=True),
        ),
    ]

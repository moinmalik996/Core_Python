# Generated by Django 4.0.2 on 2022-02-10 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stu_classes',
            new_name='stu_class',
        ),
    ]

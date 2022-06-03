# Generated by Django 4.0.4 on 2022-05-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Your Name', max_length=70)),
                ('email', models.EmailField(help_text='Enter Your Email', max_length=70)),
            ],
        ),
    ]

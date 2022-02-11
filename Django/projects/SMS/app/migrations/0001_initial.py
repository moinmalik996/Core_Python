# Generated by Django 4.0.2 on 2022-02-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=70)),
                ('stu_age', models.IntegerField()),
                ('stu_fathername', models.CharField(max_length=70)),
                ('stu_roll', models.IntegerField(unique=True)),
                ('stu_section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=100)),
                ('stu_classes', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)])),
                ('stu_city', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=70)),
                ('t_age', models.IntegerField()),
                ('t_subject', models.CharField(max_length=70)),
                ('t_salary', models.IntegerField()),
                ('t_city', models.CharField(max_length=70)),
            ],
        ),
    ]

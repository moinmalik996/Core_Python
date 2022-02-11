# Generated by Django 4.0.2 on 2022-02-10 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_stu_classes_student_stu_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stu_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_fathername',
            new_name='fathername',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_roll',
            new_name='roll',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_section',
            new_name='section',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stu_class',
            new_name='standard',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='t_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='t_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='t_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='t_salary',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='t_subject',
            new_name='subject',
        ),
    ]

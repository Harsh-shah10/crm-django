# Generated by Django 4.2 on 2023-04-30 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_course_end_date_remove_course_start_date_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='course',
            table='Course',
        ),
        migrations.AlterModelTable(
            name='tag',
            table='Tag',
        ),
    ]

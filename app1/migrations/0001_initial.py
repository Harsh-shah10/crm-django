# Generated by Django 4.2 on 2023-04-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=20)),
                ('instructor_name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('original_course_link', models.URLField()),
                ('download_link', models.URLField()),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='course_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course_tags', models.ManyToManyField(to='app1.tag')),
            ],
        ),
    ]

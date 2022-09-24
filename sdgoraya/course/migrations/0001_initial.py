# Generated by Django 4.0.3 on 2022-05-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_page_title', models.CharField(max_length=50)),
                ('course_img', models.CharField(max_length=50)),
                ('course_title', models.CharField(max_length=50)),
                ('course_desc', models.TextField()),
            ],
        ),
    ]

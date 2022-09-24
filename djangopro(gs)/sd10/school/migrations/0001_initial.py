# Generated by Django 4.0.3 on 2022-06-22 01:58

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
                ('roll_no', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('marks', models.IntegerField()),
                ('pass_date', models.DateField()),
            ],
        ),
    ]

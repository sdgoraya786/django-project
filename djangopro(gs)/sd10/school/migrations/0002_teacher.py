# Generated by Django 4.0.3 on 2022-06-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('salary', models.IntegerField()),
                ('join_date', models.DateField()),
            ],
        ),
    ]
# Generated by Django 4.0.3 on 2022-06-30 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(unique=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='division',
            field=models.CharField(default=None, max_length=70, null=True),
        ),
    ]
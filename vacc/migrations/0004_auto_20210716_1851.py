# Generated by Django 3.1.2 on 2021-07-16 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacc', '0003_auto_20210716_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Aadhar_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='details',
            name='Phone_number',
            field=models.CharField(max_length=20),
        ),
    ]

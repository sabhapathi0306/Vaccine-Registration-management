# Generated by Django 3.1.2 on 2021-07-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacc', '0006_auto_20210717_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='Dose',
            new_name='doseage',
        ),
    ]

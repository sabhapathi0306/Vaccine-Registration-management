# Generated by Django 3.1.2 on 2021-07-16 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=200)),
                ('Aadhar_number', models.IntegerField(unique=True)),
                ('Phone_number', models.IntegerField()),
                ('Vaccine', models.TextField(max_length=50)),
                ('Gender', models.TextField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Date', models.DateField()),
                ('Dose', models.TextField(max_length=50)),
            ],
        ),
    ]
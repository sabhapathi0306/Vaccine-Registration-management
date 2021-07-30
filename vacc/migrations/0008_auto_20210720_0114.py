# Generated by Django 3.1.2 on 2021-07-19 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacc', '0007_auto_20210717_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='recevied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Aadhar_number', models.CharField(max_length=20)),
                ('Phone_number', models.CharField(max_length=20)),
                ('Vaccine', models.CharField(max_length=50)),
                ('Gender', models.TextField(max_length=20)),
                ('Reg_Date', models.DateField()),
                ('doseage', models.CharField(max_length=100)),
                ('Group', models.CharField(max_length=50)),
                ('Pin', models.CharField(max_length=10)),
                ('rec_Date', models.DateField()),
            ],
            options={
                'db_table': 'vacc_recevied',
            },
        ),
        migrations.AlterField(
            model_name='details',
            name='doseage',
            field=models.CharField(max_length=100),
        ),
    ]

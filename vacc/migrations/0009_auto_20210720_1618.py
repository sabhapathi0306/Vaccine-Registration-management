# Generated by Django 3.1.2 on 2021-07-20 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacc', '0008_auto_20210720_0114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='recevied',
        ),
        migrations.AddField(
            model_name='details',
            name='Rec_Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='Status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
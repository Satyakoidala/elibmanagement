# Generated by Django 3.2.4 on 2021-06-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='amountpaid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]

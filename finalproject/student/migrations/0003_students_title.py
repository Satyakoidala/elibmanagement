# Generated by Django 3.2.4 on 2021-07-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_students_amountpaid'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='title',
            field=models.CharField(default='Mrs', max_length=4),
        ),
    ]

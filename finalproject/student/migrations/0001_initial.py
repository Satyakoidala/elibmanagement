# Generated by Django 3.2.4 on 2021-06-25 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('section', models.IntegerField(default=1)),
                ('academicyear', models.CharField(default='2017-2021', max_length=9)),
                ('amountpaid', models.IntegerField(default=0)),
                ('studid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='users.library_users')),
            ],
        ),
    ]

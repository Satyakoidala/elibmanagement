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
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalbooks', models.IntegerField(blank=True, default=0)),
                ('booksinside', models.IntegerField(blank=True, default=0)),
                ('issuedbooks', models.IntegerField(blank=True, default=0)),
                ('submittedbooks', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('issuedcount', models.IntegerField(blank=True, default=0)),
                ('retrievedcount', models.IntegerField(blank=True, default=0)),
                ('totalactions', models.IntegerField(blank=True, default=0)),
                ('libid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarians', to='users.library_users')),
            ],
        ),
    ]

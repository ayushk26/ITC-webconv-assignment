# Generated by Django 3.2.4 on 2021-06-06 15:41

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamID', models.CharField(max_length=15)),
                ('teamName', models.CharField(max_length=25)),
                ('members', django_mysql.models.ListCharField(models.CharField(max_length=25), max_length=156, size=6)),
            ],
        ),
    ]
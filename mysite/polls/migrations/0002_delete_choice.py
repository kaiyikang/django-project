# Generated by Django 4.0 on 2022-03-13 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
# Generated by Django 3.2.5 on 2021-08-01 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='create_at',
            new_name='created_at',
        ),
    ]

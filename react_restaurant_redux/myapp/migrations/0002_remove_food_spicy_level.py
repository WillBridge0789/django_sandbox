# Generated by Django 4.1.7 on 2023-03-30 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='spicy_level',
        ),
    ]

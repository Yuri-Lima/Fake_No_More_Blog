# Generated by Django 3.1.5 on 2021-01-17 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_user_full_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='full_name2',
        ),
    ]

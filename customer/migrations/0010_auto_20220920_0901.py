# Generated by Django 4.0.6 on 2022-09-20 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_remove_customerstate_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerbankaccount',
            name='shaba',
        ),
    ]

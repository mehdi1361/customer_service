# Generated by Django 4.0.6 on 2022-09-18 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_customerfund_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerstate',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerstate',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerstate',
            name='updated_at',
        ),
    ]
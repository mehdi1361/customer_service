# Generated by Django 4.0.6 on 2022-08-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_remove_customerphoneperson_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerbrokerbourseaccounts',
            name='is_default',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_basemebbcocustomergroup_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerphoneperson',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerphoneperson',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerphoneperson',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='customerphoneperson',
            name='is_mobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customerphoneperson',
            name='mebbco_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

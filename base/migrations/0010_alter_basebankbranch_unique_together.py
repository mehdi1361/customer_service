# Generated by Django 4.0.6 on 2022-08-23 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_basebankbranch_rayan_branch_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='basebankbranch',
            unique_together={('rayan_branch_id', 'bank')},
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_basebankbranch_rayan_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basebankbranch',
            name='rayan_branch_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

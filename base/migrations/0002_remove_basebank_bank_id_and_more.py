# Generated by Django 4.0.6 on 2022-08-22 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basebank',
            name='bank_id',
        ),
        migrations.RemoveField(
            model_name='basebankbranch',
            name='bank_branch_id',
        ),
        migrations.RemoveField(
            model_name='basebankbranch',
            name='bank_id',
        ),
        migrations.RemoveField(
            model_name='basecities',
            name='city_id',
        ),
        migrations.RemoveField(
            model_name='baseprovince',
            name='province_id',
        ),
        migrations.AddField(
            model_name='basebank',
            name='rayan_bank_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='basebankbranch',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.basebank'),
        ),
        migrations.AlterField(
            model_name='basebank',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='basebankbranch',
            name='rayan_bank_id',
            field=models.TextField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='basecities',
            name='rayan_city_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='baseprovince',
            name='rayan_province_id',
            field=models.IntegerField(unique=True),
        ),
    ]

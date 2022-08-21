# Generated by Django 4.0.6 on 2022-08-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_rayan_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basemebbcocustomergroup',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='basemebbcocustomergroup',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='basemebbcocustomergroup',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customeraddress',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerbankaccount',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerbankaccount',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerbankaccount',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerbranch',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerbranch',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerbranch',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerbrokerbourseaccounts',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerbrokerbourseaccounts',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerbrokerbourseaccounts',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerbrokerinfo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerbrokerinfo',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerbrokerinfo',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customercomexvisitor',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customercomexvisitor',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customercomexvisitor',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerfile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerfile',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerfile',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerfinancialinfo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerfinancialinfo',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerfinancialinfo',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerfund',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerfund',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerfund',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customerjobinfo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customerjobinfo',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='customerjobinfo',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='customerprivateinfo',
            name='sex_type_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
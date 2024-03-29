# Generated by Django 4.0.6 on 2022-11-08 07:24

from django.db import migrations


def create_data(apps, schema_editor):
    BaseFund = apps.get_model('base', 'BaseFund')
    CustomerFund = apps.get_model('customer', 'CustomerFund')

    for item in BaseFund.objects.all():
        CustomerFund.objects.filter(fund_name=item.name).update(fund=item)

class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_customerfund_fund'),
        ('base', '0016_auto_20221108_0703'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

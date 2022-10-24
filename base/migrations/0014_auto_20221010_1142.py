# Generated by Django 4.0.6 on 2022-10-10 11:42

from django.db import migrations

def create_data(apps, schema_editor):
    BaseFileType = apps.get_model('base', 'BaseFileType')
    types = [
        {"name": "signature", "fa_name": "نمونه امضا", "is_active": True, "is_force": True},
        {"name": "birth_cert_copy", "fa_name": "کپی شناسنامه", "is_active": True, "is_force": True},
        {"name": "nationa_security_card_copy", "fa_name": "کپی کارت ملی", "is_active": True, "is_force": True},
        {"name": "etc", "fa_name": "غیره", "is_active": True, "is_force": False},
    ]

    for item in types:
        BaseFileType.objects.create(**item)

class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20220928_0804'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

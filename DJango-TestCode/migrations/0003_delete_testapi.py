# Generated by Django 4.2.1 on 2023-05-25 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vftapi', '0002_remove_testapi_alias_remove_testapi_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='testApi',
        ),
    ]

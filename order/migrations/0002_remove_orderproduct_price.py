# Generated by Django 3.2.9 on 2021-11-15 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='price',
        ),
    ]
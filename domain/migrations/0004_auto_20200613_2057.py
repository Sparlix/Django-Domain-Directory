# Generated by Django 3.0.7 on 2020-06-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_auto_20200613_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='link',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='owner',
        ),
        migrations.AlterField(
            model_name='domain',
            name='expiry',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='domain',
            name='renew',
            field=models.TextField(),
        ),
    ]
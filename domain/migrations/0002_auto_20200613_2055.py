# Generated by Django 3.0.7 on 2020-06-14 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0001_initial'),
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
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='domain',
            name='renew',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
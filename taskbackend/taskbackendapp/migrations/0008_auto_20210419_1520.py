# Generated by Django 3.1.5 on 2021-04-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskbackendapp', '0007_auto_20210418_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='results',
            field=models.TextField(default='Not Set', verbose_name='Algorithm Text Output'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-21 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_auto_20180921_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_created',
            field=models.DateTimeField(auto_created=True),
        ),
    ]

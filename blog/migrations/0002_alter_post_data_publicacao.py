# Generated by Django 4.1.3 on 2022-11-08 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 8, 20, 37, 22, 160507)),
        ),
    ]

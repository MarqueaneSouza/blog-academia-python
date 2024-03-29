# Generated by Django 4.1.3 on 2022-12-29 20:44

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_conteudo_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem_capa',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog/'),
        ),
        migrations.AddField(
            model_name='post',
            name='resumo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 20, 44, 24, 943176, tzinfo=datetime.timezone.utc)),
        ),
    ]

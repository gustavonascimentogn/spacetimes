# Generated by Django 3.0.5 on 2021-02-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0002_auto_20210213_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='processado',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.0.5 on 2021-02-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0015_auto_20210215_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='ultimo_evento',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Última ocorrência na Task'),
        ),
    ]
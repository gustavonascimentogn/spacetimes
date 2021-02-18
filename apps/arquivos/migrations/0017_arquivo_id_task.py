# Generated by Django 3.0.5 on 2021-02-16 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_results', '0007_remove_taskresult_hidden'),
        ('arquivos', '0016_arquivo_ultimo_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='id_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_celery_results.TaskResult', verbose_name='Resultados de execução da Task'),
        ),
    ]

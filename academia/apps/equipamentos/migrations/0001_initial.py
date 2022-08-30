# Generated by Django 4.0.5 on 2022-08-29 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=16, verbose_name='Nome do Equipamento')),
                ('descr', models.CharField(max_length=200, verbose_name='Descrição')),
                ('status', models.CharField(choices=[('Funcionando', 'Funcionando'), ('Manutenção', 'Manutenção'), ('Quebrado', 'Quebrado')], max_length=11)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='static/img')),
            ],
        ),
    ]

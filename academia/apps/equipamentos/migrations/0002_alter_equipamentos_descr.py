# Generated by Django 4.0.5 on 2022-08-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamentos',
            name='descr',
            field=models.CharField(max_length=200, verbose_name='Descrição'),
        ),
    ]

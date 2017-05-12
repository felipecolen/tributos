# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('pessoa_cpf', models.CharField(max_length=15)),
                ('pessoa_nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Tributos',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('is_pago', models.BooleanField(verbose_name='Pago?')),
                ('taxas_impostos', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('veiculo_placa', models.CharField(max_length=7)),
                ('veiculo_preco_fipe', models.CharField(max_length=10)),
                ('fk_pessoa', models.ForeignKey(to='apptributo.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='tributos',
            name='fk_veiculo',
            field=models.ForeignKey(to='apptributo.Veiculo'),
        ),
    ]

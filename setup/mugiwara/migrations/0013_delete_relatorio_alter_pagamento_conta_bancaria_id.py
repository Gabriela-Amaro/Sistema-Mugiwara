# Generated by Django 5.1.1 on 2024-10-17 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mugiwara', '0012_alter_pagamento_conta_bancaria_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='relatorio',
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='conta_bancaria_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mugiwara.conta_bancaria'),
        ),
    ]

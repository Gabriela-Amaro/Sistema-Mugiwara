# Generated by Django 5.1.1 on 2024-10-17 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mugiwara', '0011_alter_pagamento_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='conta_bancaria_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mugiwara.conta_bancaria'),
        ),
    ]

# Generated by Django 5.2.1 on 2025-05-19 01:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastroveiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('ano', models.IntegerField()),
                ('cor', models.CharField(blank=True, max_length=30, null=True)),
                ('renavam', models.CharField(blank=True, max_length=20, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

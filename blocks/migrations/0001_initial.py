# Generated by Django 5.1.6 on 2025-02-10 16:24

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('number', models.PositiveIntegerField()),
                ('blockchain_created_at', models.DateTimeField(default=None, null=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blocks', to='common.currency')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blocks', to='providers.provider')),
            ],
            options={
                'verbose_name': 'Block',
                'verbose_name_plural': 'Blocks',
                'db_table': 'blocks',
            },
        ),
    ]

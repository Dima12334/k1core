# Generated by Django 5.1.6 on 2025-02-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blocks", "0001_initial"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="block",
            name="number",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name="block",
            unique_together={("currency", "number")},
        ),
    ]

# Generated by Django 3.0.5 on 2020-05-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meals", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="amount",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]

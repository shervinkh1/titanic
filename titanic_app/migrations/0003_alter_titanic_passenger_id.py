# Generated by Django 5.0.6 on 2024-08-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("titanic_app", "0002_alter_titanic_passenger_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="titanic",
            name="passenger_id",
            field=models.IntegerField(unique=True),
        ),
    ]

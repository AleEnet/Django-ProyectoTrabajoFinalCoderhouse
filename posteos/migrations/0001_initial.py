# Generated by Django 4.1.5 on 2023-01-05 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("subtitulo", models.CharField(max_length=100)),
                ("cuerpo", models.TextField()),
                ("autor", models.CharField(max_length=50)),
                ("fecha", models.DateField(verbose_name=datetime.date.today)),
                ("imagen", models.ImageField(upload_to="posteos-imagen")),
            ],
        ),
    ]
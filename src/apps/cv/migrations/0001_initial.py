# Generated by Django 3.0.5 on 2020-04-20 17:03

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Techno",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.DateField(unique=True)),
                ("description", models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start", models.DateField(blank=True, null=True)),
                ("end", models.DateField(blank=True, null=True)),
                ("summary", models.TextField(null=True, unique=True)),
                (
                    "technos",
                    models.ManyToManyField(related_name="projects", to="cv.Techno"),
                ),
            ],
        ),
    ]
